import pandas as pd
import numpy as np
from sklearn import linear_model

data = pd.read_csv('../data_all.csv')

x = data[['tempo', 'popularity','energy','dance','valence','instrumental','acoustic']]

y = data['health']

clf = linear_model.LinearRegression()

clf.fit(x,y)

print(clf.coef_)
print(clf.get_params())
print(clf.score(x,y))