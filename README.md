# Fifa_Player_OverAll_Rating_Prediction

## What kind of data are we using?

I found a large dataset of the FIFA games on Kaggle. The dataset consists of data from FIFA 15 to FIFA 20. We will be using the latest FIFA game in the dataset which is FIFA 20. The dataset can be downloaded from [Kaggle](https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset). The dataset consists of 18,278 rows and 104 columns. The columns contain features such as Player Name, Age, Height, Weight, Nationality, and many more. Since we are trying to predict the overall rating, we would only need to focus on the features that have correlations with the overall rating, but we’ll get to that later.


## Define the Problem

The first thing that any ML Engineer should do is to define the problem. For this project, the problem we are facing is accurately predicting the player ratings without having to hard code an algorithm, so building a workable ML model should be our end goal. In FIFA 20, a player’s overall score is defined by the score of each player attribute such as Pace, Shooting, Passing, Dribbling, and many others. We are trying to predict the overall score based on the player’s offensive and defensive attributes. The data already comes with labeled training examples which means we are dealing with a supervised learning problem. It is also a typical regression task since we are tasked with predicting a value. More specifically, this is a multiple regression problem since the model will use multiple features to make a prediction.

## Select a Performance Measure

Now that we have defined the problem, we need to select a performance measure. I like to use the Root Mean Square Error (RMSE). This is the preferred performance measure for regression problems. The RMSE is a measure of how well the model performed. It gives an idea of how much error the system makes in its prediction. RMSE is the calculation of the residuals (prediction errors) with respect to the line of best fit. The formula can be seen below:
![1 st1zZN7rHX8KYy_BZWYETg](https://user-images.githubusercontent.com/115188345/194416690-4857ff93-f9b0-40e1-9005-f14cff053a06.png)
