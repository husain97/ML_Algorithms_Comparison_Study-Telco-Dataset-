# -*- coding: utf-8 -*-
"""DecisionTreeClassifier(Telco Dataset).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lSnAsYluPfeTR_sbPvf5qGcz1wBwhRNW
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

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

pd.set_option('display.max_columns', None)  
print(Y_pred[0:5])

from sklearn import metrics
print("Accuracy:",(round(metrics.accuracy_score(Y_test,Y_pred) * 100)), "%")
print("Confusion Matrix For UNPRUNED TREE:")
metrics.confusion_matrix(Y_test, Y_pred)

#Visualizing DecisionTree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = features_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('telco.png')
Image(graph.create_png())

#Pruning the tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

model = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

pd.set_option('display.max_columns', None)  
#print(X_test[0:19])
print(Y_pred[0:5])

from sklearn import metrics
print("Accuracy:",(round(metrics.accuracy_score(Y_test,Y_pred) * 100)), "%")
print("Confusion Matrix For PRUNED TREE:")
metrics.confusion_matrix(Y_test, Y_pred)

#Visualizing DecisionTree-Prunned
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = features_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('telco.png')
Image(graph.create_png())