# Feature Importance
import pandas as pd 
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

# load the iris datasets
dataset = pd.read_csv('data_all_norm.csv')

x = dataset[['tempo', 'popularity','energy', 'liveness', 'dance', 'valence', 'instrumental', 'acoustic']]
y = dataset['health']

print(x)
print(y)	

# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression()

# create the RFE model and select 3 attributes
rfe = RFE(model, 1)
rfe = rfe.fit(x, y)

# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)