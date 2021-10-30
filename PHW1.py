import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/seoyo/Desktop/2021-2학기/머신러닝/archive/adult.csv")
print(df.info())

#To Fill in the wrong value
df['workclass'] = df['workclass'].replace('?','Private')
df['occupation'] = df['occupation'].replace('?','Prof-specialty')
df['native-country'] = df['native-country'].replace('?','United-States')

#To define income(Target) encoding
df.income = df.income.replace('<=50K', 0)
df.income = df.income.replace('>50K', 1)

categorical = [var for var in df.columns if df[var].dtype=='O']
numerical = [var for var in df.columns if df[var].dtype!='O']

#To check missing value 

df[categorical].isnull().sum()
df[numerical].isnull().sum()

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder
df = df.apply(LabelEncoder().fit_transform)

#To split test, train dataset
X = df.drop(['income'], axis=1)
y = df['income']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Scaling data
cols = X_train.columns
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])

#Using naive_bayes model
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

from sklearn.metrics import accuracy_score

print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

y_pred_train = gnb.predict(X_train)

print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train)))

