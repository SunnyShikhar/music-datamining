import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv('data_all.csv')

x = data[['energy', 'liveness', 'dance', 'valence', 'instrumental', 'acoustic']]
y = data['health']

data.head()

x = sm.add_constant(x)
allVars = sm.OLS(y,x).fit()

print(allVars.summary())