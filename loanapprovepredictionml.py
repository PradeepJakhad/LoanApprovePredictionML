# -*- coding: utf-8 -*-
"""LoanApprovePredictionML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qS1mZwPJ1cFOOhd95SljJ8q26eER3UoL
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('/content/drive/MyDrive/LoanApprovalPrediction.csv')

df.head()

objec=(df.dtypes=='object')
print("Categorical variables:",len(list(objec[objec].index)))

df.drop('Loan_ID',inplace=True,axis=1)

obj = (df.dtypes == 'object')
object_cols = list(obj[obj].index)
plt.figure(figsize=(18,36))
index = 1

for col in object_cols:
  y = df[col].value_counts()
  plt.subplot(11,4,index)
  plt.xticks(rotation=90)
  sns.barplot(x=list(y.index), y=y)
  index +=1

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
obj = (df.dtypes == 'object')
for col in list(obj[obj].index):
  df[col] = label_encoder.fit_transform(df[col])

df.head(10)

obj = (df.dtypes == 'object')
print("Categorical variables:",len(list(obj[obj].index)))

plt.figure(figsize=(12,6))

sns.heatmap(df.corr(),cmap='BrBG',fmt='.2f',
            linewidths=2,annot=True)

sns.barplot(x="Gender",y="Married",hue="Loan_Status",data=df)

sns.boxplot(df['ApplicantIncome'],palette='rainbow')

for col in df.columns:
  df[col]=df[col].fillna(df[col].mean())

df.isnull().sum()

from sklearn.model_selection import train_test_split

X = df.drop(['Loan_Status'],axis=1)
Y = df['Loan_Status']
X.shape,Y.shape

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size=0.4,
                                                    random_state=1)
X_train.shape, X_test.shape, Y_train.shape, Y_test.shape

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=3)
rfc = RandomForestClassifier(n_estimators = 10,
                             criterion = 'entropy',
                             random_state =10)
svc = SVC()
lc = LogisticRegression()

# making predictions on the training set
for clf in (rfc, knn, svc,lc):
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_train)
    print("Accuracy score of ",
          clf.__class__.__name__,
          "=",100*metrics.accuracy_score(Y_train,
                                         Y_pred))

for clf in (rfc, knn, svc,lc):
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    print("Accuracy score of ",
          clf.__class__.__name__,"=",
          100*metrics.accuracy_score(Y_test,
                                     Y_pred))