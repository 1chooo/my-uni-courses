import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("./train_data_titanic.csv")
df.head()
df.info()

df.drop(["Name", "Ticket"], axis = 1, inplace = True)
df.drop("Cabin", axis = 1, inplace = True)

df["Embarked"].value_counts().idxmax()
df["Embarked"].fillna(df["Embarked"].value_counts().idxmax(),inplace = True) 
df["Embarked"].value_counts()


df["Age"].isnull().value_counts()
df.groupby("Sex")["Age"].median().plot(kind = "bar")
df["Age"] = df.groupby("Sex")["Age"].apply(lambda x: x.fillna(x.median()))
df.groupby("Sex")["Age"].median()

df.head()
df.isnull().sum()


df = pd.get_dummies(data = df, columns = ["Sex", "Embarked"])
df.head()

df.drop("Sex_female", axis = 1, inplace = True)

df.head()
df.groupby("Survived").mean()
df["PassengerId"].value_counts()
df["Pclass"].value_counts()
df["SibSp"].value_counts()
df["Parch"].value_counts()
df["Fare"].value_counts()

df.corr()

x = df.drop(["Survived", "Pclass"], axis = 1)
y = df["Survived"]

from sklearn.model_selection import train_test_split

""" Split to training and testing data. """
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 99)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train, y_train)
predictions = lr.predict(x_test)


from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score 
accuracy_score(y_test, predictions)
recall_score(y_test, predictions)
precision_score(y_test, predictions)
pd.DataFrame(confusion_matrix(y_test, predictions), columns=['Predict not Survived', 'Predict Survived'], index=['True not Survived', 'True Survived'])

import joblib 
joblib.dump(lr,'Titanic-LR-20220409.pkl',compress = 3)