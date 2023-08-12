import joblib
import pandas as pd

model_pretrained = joblib.load("Titanic-LR-20220409.pkl")

df_test = pd.read_csv("./test.csv") 
df_test.drop(['Name','Ticket'],axis=1,inplace=True) 
df_test.drop('Cabin',axis=1,inplace=True)
df_test['Age'] = df_test.groupby('Sex')['Age'].apply(lambda x: x.fillna(x.median()))
df_test.isnull().sum()
df_test['Fare'].value_counts() 
df_test['Fare'].fillna(df_test['Fare'].value_counts().idxmax(),inplace=True)
df_test = pd.get_dummies(data=df_test, columns=['Sex','Embarked']) 
df_test.drop('Sex_female',axis=1,inplace=True)
df_test.drop('Pclass',axis=1,inplace=True)

predictions2 = model_pretrained.predict(df_test) 
predictions2
#Preare submit file
forSubmissionDF = pd.DataFrame(columns=['PassengerId','Survived']) 
forSubmissionDF['PassengerId'] = range(892,1310) 
forSubmissionDF['Survived'] = predictions2
forSubmissionDF
forSubmissionDF.to_csv('for_submission_20220409.csv', index=False)