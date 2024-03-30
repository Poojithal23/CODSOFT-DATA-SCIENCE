# -*- coding: utf-8 -*-
"""TASK_1_TITANIC_SURVIVAL_PREDICTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Poojithal23/CODSOFT-DATA-SCIENCE/blob/main/TASK_1_TITANIC_SURVIVAL_PREDICTION.ipynb

Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

"""Importing DATASET"""

from google.colab import files

#upload your CSV file
uploaded = files.upload()

#read the uploaded CSV file into a dataframe
df = pd.read_csv(io.BytesIO(uploaded["Titanic-Dataset (2).csv"]))

#display the dataframe
df.head(10)

df.shape

df.describe()

df["Survived"].value_counts()

"""Visualization number of survivals"""

sns.countplot(x=df['Survived'], hue=df['Pclass'])

df['Sex']

"""Visualization count of survivals wrt gender"""

sns.countplot(x=df['Sex'], hue=df['Survived'])

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
df['Sex']=lb.fit_transform(df['Sex'])
df.head()

"""Model Training"""

x=df[['Pclass','Sex']]
y=df['Survived']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
log=LogisticRegression(random_state=0)
log.fit(x_train,y_train)

predictions=log.predict(x_test)
print(predictions)
print(y_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,predictions)
print(f"Accuracy:{accuracy}")

import warnings
warnings.filterwarnings("ignore")
res=log.predict([[2,1]])
if(res==0):
  print("sorry!not survived")
else:
  print("survived")