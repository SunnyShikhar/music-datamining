import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
import pylab as P
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

dataset = pd.read_csv('linear_regression_cleaned.csv')
print(dataset)

# scatter plot with color based on a categorical variable
# create a grid first and then map the graph to this grid
attend_class = [0,1]
kws = dict(s=75, linewidth=1, edgecolor="w")
fg = sns.FacetGrid(data=dataset, hue='attend_class', hue_order=attend_class, palette="Set1")
fg.map(plt.scatter, 'extra_hours', 'grade', **kws).add_legend()
plt.show()

#pre-processing features
extra_hours =  dataset.extra_hours.reshape((len(dataset.extra_hours), 1))
attend_class =  dataset.attend_class.reshape((len(dataset.attend_class), 1))

#encode categorical variable
enc = preprocessing.OneHotEncoder()
enc.fit(attend_class)
transfomed_attend_class = enc.transform(attend_class).toarray()
print("The transformed attend class is:",transfomed_attend_class)

# prepare datasets to be fed in the regression model
CV =  dataset.grade.reshape((len(dataset.grade), 1))
data = np.concatenate((extra_hours, transfomed_attend_class), axis=1)
print("The processed dataset: ", np.concatenate((data, CV), axis=1))

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(data, CV)

# get the predictions on the training data
predicted_results = regr.predict(data)

print("Results:")
# The coefficients (m, b) of y = mx + b
print('Coefficients (m1, m2, m3): \n', regr.coef_)
print('Intercept (b): \n', regr.intercept_)

print("Mean residual sum of squares = %.2f"
      % np.mean((regr.predict(data) - CV) ** 2))
print('R2 = %.2f' % regr.score(data,CV))

plt.figure(2)
#just for demonstration
x = np.arange(140)
#line only due to extra_hours
y = 0.45*x + 34.96
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-')
plt.scatter(dataset.extra_hours[dataset.attend_class == 0], dataset.grade[dataset.attend_class == 0], color='red')
plt.scatter(dataset.extra_hours[dataset.attend_class == 1], dataset.grade[dataset.attend_class == 1], color='blue', s = 100)
plt.xlabel("extra_hours")
plt.ylabel("grades")
plt.show()


plt.figure(3)
#what is really happening
x = np.arange(140)
y_attend_class = 0.45*x + 34.96 + 5.81*1
m, b = np.polyfit(x, y_attend_class, 1)
plt.plot(x, y_attend_class, '.', color='blue')
plt.plot(x, m*x + b, '-', color = 'blue')

y_not_attend_class = 0.45*x + 34.96 - 5.81*1
m, b = np.polyfit(x, y_not_attend_class, 1)
plt.plot(x, y_not_attend_class, '.', color = 'red')
plt.plot(x, m*x + b, '-', color = 'red')

plt.scatter(dataset.extra_hours[dataset.attend_class == 0], dataset.grade[dataset.attend_class == 0], color='red')
plt.scatter(dataset.extra_hours[dataset.attend_class == 1], dataset.grade[dataset.attend_class == 1], color='blue')
plt.xlabel("extra_hours")
plt.ylabel("grades")
plt.show()


# to see how the residual errors behave
residual_error = CV - predicted_results
print("Mean of residuals =", np.mean(residual_error))
print("Standard deviation of residuals =", np.std(residual_error))

# residual plot of error vs. extra hours
plt.figure(4)
plt.plot((-40,140),(0,0), 'r--')
plt.scatter(extra_hours,residual_error,label='residual error')
plt.title("Residual plot")
plt.xlabel("extra_hours")
plt.ylabel("residual error")
plt.show()

# residual plot of error vs. attend class or no?
plt.figure(5)
plt.plot((-0.5,1.5),(0,0), 'r--')
plt.scatter(attend_class,residual_error,label='residual error')
plt.title("Residual plot")
plt.xlabel("attend_class")
plt.ylabel("residual error")
plt.show()

# distribution of residuals
plt.figure(6)
plt.hist(residual_error)
plt.title("Distribution of residuals")
plt.xlabel("residual error")
plt.show()

# distribution of residuals with normal distribution
plt.figure(7)
n, bins, patches = plt.hist(residual_error, 10, normed=1,  alpha = 0.5)
y_pdf = P.normpdf(bins, np.mean(residual_error), np.std(residual_error))
l = P.plot(bins, y_pdf, 'k--', linewidth=1.5)
plt.show()

print("If a person studies for 75 hours and does not come to class: grade: %.2f" % regr.predict([100, 1, 0]))
print("If a person studies for 45 hours and comes to class: grade: %.2f" % regr.predict([70, 0, 1]))