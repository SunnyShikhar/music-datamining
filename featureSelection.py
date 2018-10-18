# Feature Importance
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

# load the iris datasets
dataset = pd.read_csv('data/master.csv')
dataset = dataset.dropna()

x = dataset[['tempo', 'popularity','energy', 'liveness', 'dance', 'valence', 'instrumental', 'acoustic']]
y = dataset['health_categorical']

# Normalize all data for model
sc = StandardScaler()  
x_norm = sc.fit_transform(x) 

# create a base classifier used to evaluate a subset of attributes

# Recursively remove attributes and build a model on those attributes that remain, 
# using model accuracy to find attributes (combination of attributes)
model = LogisticRegression()

# create the RFE model and list order of importance
rfe = RFE(model, 1)
rfe = rfe.fit(x_norm, y)

# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)