import streamlit as st
import pandas as pd
import numpy as np


url = "https://drive.google.com/file/d/1b-1D2i76zQvavE9pG6zqqOQha6S1mxpp/view?usp=sharing"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

player_data = pd.read_csv(path)

st.write(player_data.head())
st.write(player_data.columns)


columns = ['Overall','Dribbling','ShortPassing','Reactions','Agility','FKAccuracy','BallControl','Crossing','Strength','Acceleration','Finishing','Stamina','SprintSpeed','LongPassing','Special','Potential','ShotPower']

player_df = player_data[columns]

player_df.columns = ['overall','skill_dribbling','attacking_short_passing','movement_reactions','movement_agility','attacking_heading_accuracy','skill_ball_control','attacking_crossing','power_strength','movement_acceleration','attacking_finishing','power_stamina','movement_sprint_speed','skill_long_passing','special','potential','power_shot_power']


player_df= player_df.replace(0, pd.np.nan)

player_df.dropna(inplace=True)

def outliers(col):
    q1 = np.nanpercentile(col, 25)
    q3 = np.nanpercentile(col, 75)
    iqr = q3 - q1
    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)
    return lower , upper

lp, hp = outliers(player_df['overall'])

from sklearn.preprocessing import FunctionTransformer


def remove_outliers(X):
    lower, upper = outliers(player_df['overall'])
    X = X[(player_df['overall'] <= upper) & (player_df['overall'] > 0)]
    return X
remove_outliers_y = FunctionTransformer(remove_outliers, validate=False)


from sklearn.model_selection import train_test_split
train_val_set, test_set = train_test_split(player_df, test_size=0.2, random_state=42, shuffle = True)

train_set, val_set = train_test_split(train_val_set, test_size=0.2, random_state=42, shuffle = True)

train_set = remove_outliers_y.fit_transform(train_set)
val_set = remove_outliers_y.fit_transform(val_set)
test_set = remove_outliers_y.fit_transform(test_set)

y_train = train_set['overall']
X_train = train_set.drop(['overall'], axis=1)

y_valid = val_set['overall']
X_valid = val_set.drop(['overall'], axis=1)

y_test = test_set['overall']
X_test = test_set.drop(['overall'], axis=1)


X_train = pd.DataFrame(X_train)
X_valid = pd.DataFrame(X_valid)
X_test = pd.DataFrame(X_test)


from sklearn.preprocessing import MinMaxScaler
normalize = MinMaxScaler()

X_train_normalized = pd.DataFrame(normalize.fit_transform(X_train), columns = X_train.columns)
X_valid_normalized = pd.DataFrame(normalize.fit_transform(X_valid), columns = X_valid.columns)
X_test_normalized = pd.DataFrame(normalize.fit_transform(X_test), columns = X_test.columns)


st.sidebar.header('Specify input parameters')

from sklearn.ensemble import RandomForestRegressor

from sklearn.feature_selection import RFECV

min_features_to_select = 5  # Minimum number of features to consider
rf = RandomForestRegressor(n_estimators=10, random_state=42)
rfecv = RFECV(estimator=rf, step=1, cv=10,
              scoring='neg_mean_squared_error',
              min_features_to_select=min_features_to_select)
rfecv_fitted =rfecv.fit(X_train_normalized, y_train)

import pickle

with open('model_pickle_3','wb') as f:
    pickle.dump(rfecv_fitted,f)