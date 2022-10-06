import streamlit as st
import pandas as pd

import numpy as np
import sklearn
import pickle

with open('model_pickle_3','rb') as f:
    Rmodel=pickle.load(f)

st.image("https://wallpaperaccess.com/full/3016184.jpg")

st.write("""This Application can be used for predicting the overall rating of any player, given these features on the left with great accuracy. 

Managers, Scouts, Academy owners, national team Coaches can deploy this application to return an unbaised overall rating for any player, and make suitable decisions accordingly""")

st.title('player prediction')

st.sidebar.header('player data')

def user_report():
    skill_dribbling= st.sidebar.slider('skill_dribbling',min_value =0.0,max_value=1.0,step=0.001)
    
    attacking_short_passing = st.sidebar.slider('attacking_short_passing',min_value=0.0,max_value=1.0,step=0.001)

    movement_reactions= st.sidebar.slider('movement_reactions',min_value=0.0,max_value=1.0,step =0.001)

    movement_agility= st.sidebar.slider('movement_agility',min_value=0.0,max_value=1.0,step=0.001)

    attacking_heading_accuracy=st.sidebar.slider('attacking_heading_accuracy',min_value=0.0,max_value=1.0,step=0.001)

    skill_ball_control=st.sidebar.slider('skill_ball_control',min_value=0.0,max_value=1.0,step=0.001)

    attacking_crossing=st.sidebar.slider('attacking_crosiing',min_value=0.0,max_value=1.0,step=0.001)

    power_strength=st.sidebar.slider('power_strenght',min_value=0.0,max_value=1.0,step=0.001)

    movement_acceleration=st.sidebar.slider('movement_acceleration',min_value=0.0,max_value=1.0,step=0.001)

    attacking_finishing=st.sidebar.slider('attacking_finishing',min_value=0.0,max_value=1.0,step=0.001)

    power_stamina=st.sidebar.slider('power_stamina',min_value=0.0,max_value=1.0,step=0.001)

    movement_sprint_speed=st.sidebar.slider('movement_sprint_speed',min_value=0.0,max_value=1.0,step=0.001)

    skill_long_passing=st.sidebar.slider('skill_long_passing',min_value=0.0,max_value=1.0,step=0.001)

    special=st.sidebar.slider('special',min_value=0.0,max_value=1.0,step=0.001)

    potential=st.sidebar.slider('potential',min_value=0.0,max_value=1.0,step=0.001)

    power_shot_power=st.sidebar.slider('power_shot_power',min_value=0.0,max_value=1.0,step=0.001)


    user_report_data = {
        'skill_dribbling': skill_dribbling,
        'attacking_short_passing':attacking_short_passing,
        'movement_reactions': movement_reactions,
        'movement_agility': movement_agility,
        'attacking_heading_accuracy': attacking_heading_accuracy,
        'skill_ball_control': skill_ball_control,
        'attacking_crossing' : attacking_crossing,
        'power_strength': power_strength,
        'movement_acceleration':movement_acceleration,
        'attacking_finishing': attacking_finishing,
        'power_stamina': power_stamina,
        'movement_sprint_speed': movement_sprint_speed,
        'skill_long_passing': skill_long_passing,
        'special':special,
        'potential':potential,
        'power_shot_power': power_shot_power
    }
    report_data =pd.DataFrame(user_report_data, index =[0])
    return report_data

user_data = user_report()
st.header('player data')
st.write(user_data)

OverallR = Rmodel.predict(user_data)
st.subheader('player overall rating')
st.subheader(str(OverallR))