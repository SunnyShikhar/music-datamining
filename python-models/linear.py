import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import pylab as P
import seaborn as sns

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('data_all.csv')
# print(dataset)

data = dataset.dance.reshape((len(dataset.dance), 1))
CV = dataset.health.reshape((len(dataset.health), 1))

regr = linear_model.LinearRegression()
regr.fit(data,CV)
predicted_results = regr.predict(data)

plt.figure(1)
plt.plot(data, predicted_results, color = 'green', linewidth =3)
plt.scatter(data, CV, color='black')
plt.title('Mental health as a function of song dance level')
plt.xlabel('dance level')
plt.ylabel('health')
plt.show()

print("Result with Outlier:")
print('Coefficients (m): \n', regr.coef_)
print('Intercept (b): \n', regr.intercept_)

MSE = mean_squared_error(CV, predicted_results)
RMSE = math.sqrt(MSE)

R2 = r2_score(CV, predicted_results)

print("Mean residual sum of squares =", MSE)
print("RMSE =", RMSE)
print("R2 =", R2)
print("Mean residual sum of squares = %.2f" % np.mean((regr.predict(data) - CV) **2))
print('R2 = %.2f' % regr.score(data, CV))

residual_error = CV - predicted_results
print("Mean of residuals =", np.std(residual_error))
print("standard deviation of residuals =", np.std(residual_error))

plt.figure(2)
plt.plot((0,1),(0,0), 'r--')
plt.scatter(data, residual_error, label='residual error')
plt.title("Residual plot")
plt.xlabel("dance")
plt.ylabel("residual error")
plt.show()

plt.figure(3)
plt.hist(residual_error)
plt.title("Distribution of residuals")
plt.title("residual error")
plt.show()

plt.figure(4)
n, bins, patches = plt.hist(residual_error, 10, normed=1, alpha = 0.5)
y_pdf = P.normpdf(bins, np.mean(residual_error), np.std(residual_error))
l = P.plot(bins, y_pdf, 'k--', linewidth=1.5)
plt.show()













