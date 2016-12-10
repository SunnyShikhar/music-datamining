import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

data = pd.read_csv('../data_all.csv')

dataset = data[data['traumatic_experience'] == 'Yes']

x = dataset[['energy', 'dance', 'popularity', 'tempo', 'valence']]

y = dataset['health']

x = sm.add_constant(x)
allVars = sm.OLS(y,x).fit()

print(allVars.summary())