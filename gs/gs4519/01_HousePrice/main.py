# -*- coding: utf-8 -*-

"""
This code is from the machine learning course
and the main goal of this code is to predict
the trend of the house price.
"""

import matplotlib as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("./Housing_Dataset_Sample.csv")

df.head()
df.describe().T
sns.displot(df["Price"])
sns.jointplot(df["Avg. Area Income"], df["Price"])
sns.pairplot(df)

x = df.iloc[:, :5]
y = df["Price"]

""" Split to training data and testing data. """
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 54)

""" linear regression model """
from sklearn.linear_model import LinearRegression   

reg  = LinearRegression()
reg.fit(x_train, y_train)

predictions = reg.predict(x_test)       # the result
predictions

from sklearn.metrics import r2_score 
r2_score(y_test, predictions) 
plt.pyplot.scatter(y_test, predictions, color='blue')