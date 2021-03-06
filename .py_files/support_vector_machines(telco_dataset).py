# -*- coding: utf-8 -*-
"""Support Vector Machines(Telco Dataset).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BjzBM6yHdnyaRboVi5VRWPqaPxLX18_f
"""

import pandas as pd
import numpy as np
from google.colab import files
uploaded = files.upload()

data_pd = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv', index_col=False)
df = data_pd
for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes
with np.printoptions(threshold=np.inf):
  print(df.columns)

features_cols = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

X = df[features_cols]
Y = df.Churn

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

#SVM - Linear Example
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

from sklearn import svm
svm_model = svm.SVC(kernel='linear', gamma='auto')
svm_model.fit(X_train, Y_train)
Y_pred_svm = svm_model.predict(X_test)
print(Y_pred_svm)

from sklearn import metrics
print("Accuracy:",(round(metrics.accuracy_score(Y_test,Y_pred_svm) * 100)), "%")

#SVM - Sigmoid Example
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

from sklearn import svm
svm_model = svm.SVC(kernel='sigmoid', gamma='auto')
svm_model.fit(X_train, Y_train)

Y_pred_svm = svm_model.predict(X_test)
print(Y_pred_svm)

from sklearn import metrics
print("Accuracy:",(round(metrics.accuracy_score(Y_test,Y_pred_svm) * 100)), "%")

#SVM - RBF Example
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

from sklearn import svm
svm_model = svm.SVC(kernel='rbf', gamma='auto')
svm_model.fit(X_train, Y_train)

Y_pred_svm = svm_model.predict(X_test)
print(Y_pred_svm)

from sklearn import metrics
print("Accuracy:",(round(metrics.accuracy_score(Y_test,Y_pred_svm) * 100)), "%")