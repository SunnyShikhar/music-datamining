# Feature Importance
import pandas as pd 
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier


# load the iris datasets
dataset = pd.read_csv('data_all_norm.csv')

x = dataset[['tempo', 'popularity','energy', 'liveness', 'dance', 'valence', 'instrumental', 'acoustic']]
y = dataset['health']

print(x)
print(y)

# fit an Extra Trees model to the data
model = ExtraTreesClassifier()
model.fit(x, y)

# display the relative importance of each attribute
print(model.feature_importances_)