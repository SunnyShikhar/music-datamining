import pandas as pd
import matplotlib.pyplot as plt
import math
import pylab as P
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

dataset = pd.read_csv('data-files/data_all.csv')
maleDataset = dataset[dataset['gender'] == 'Male']

print(maleDataset)

#plot a scatter plot
plt.figure(1)
plt.scatter(maleDataset.tempo, maleDataset.health,  color='red')
plt.title("Male Health as a function of Tempo")
plt.xlabel("Tempo")
plt.ylabel("Total Health")
plt.show()

# fit a line to this data
# reshape data and CV to be a matrix again
data = maleDataset.tempo.reshape(len(maleDataset.tempo), 1)
CV = maleDataset.health.reshape(len(maleDataset.health), 1)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(data, CV)

# get the predictions on the training data
predicted_results = regr.predict(data)

print("Results with outlier:")
# The coefficients (m, b) of y = mx + b
print('Coefficients (m): \n', regr.coef_)
print('Intercept (b): \n', regr.intercept_)

# The mean square error MSE or the mean residual sum of square of errors should be less
MSE = mean_squared_error(CV,predicted_results)
RMSE = math.sqrt(MSE)
# Explained variance score: 1 is perfect prediction
R2 = r2_score(CV,predicted_results)

print("Mean residual sum of squares =", MSE)
print("RMSE =", RMSE)
print("R2 =", R2)
print("Mean residual sum of squares = %.2f"
      % np.mean((regr.predict(data) - CV) ** 2))
print('R2 = %.2f' % regr.score(data,CV))

plt.plot(data, predicted_results, color='green', linewidth=3)
plt.scatter(data, CV, color='black')
plt.xlabel("extra_hours")
plt.ylabel("grades")
plt.show()

# to see how the residual errors behave
residual_error = CV - predicted_results
print("Mean of residuals =", np.mean(residual_error))
print("Standard deviation of residuals =", np.std(residual_error))

plt.figure(3)
plt.plot((-40,140),(0,0), 'r--')
plt.scatter(data,residual_error,label='residual error')
plt.title("Residual plot")
plt.xlabel("extra_hours")
plt.ylabel("residual error")
plt.show()

plt.figure(4)
plt.hist(residual_error)
plt.title("Distribution of residuals")
plt.xlabel("residual error")
plt.show()

plt.figure(5)
n, bins, patches = plt.hist(residual_error, 10, normed=1,  alpha = 0.5)
y_pdf = P.normpdf(bins, np.mean(residual_error), np.std(residual_error))
l = P.plot(bins, y_pdf, 'k--', linewidth=1.5)
plt.show()

# print("If a person studies for 20 hours, what do you predict about his grade: %.2f" % regr.predict(20))
# print("If a person studies for 50 hours, what do you predict about his grade: %.2f" % regr.predict(50))
# print("If a person studies for 80 hours, what do you predict about his grade: %.2f" % regr.predict(80))
# print("In the training dataset, 80 hours of effort results in a 69.5%")
# print("If a person studies for 95 hours, what do you predict about his grade: %.2f" % regr.predict(95))
# print("If a person studies for 142 hours, what do you predict about his grade: %.2f" % regr.predict(142))