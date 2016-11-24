import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB

dataset = pd.read_csv('data_all.csv')
print(dataset)

#prepare datasets to be fed into the naive bayes model
#Predict mental health category given dance and energy

CV = dataset.resilience_cat.reshape(len(dataset.resilience_cat),1)
print(CV)
data = (dataset.ix[:,['dance','energy']].values).reshape(len(dataset.dance),2)
print(data)

#Create the model object
NB = GaussianNB()

#Train the model using the training sets
NB.fit(data,CV)

#Model
print("Probability of the classes: ", NB.class_prior_)
print("Mean of each feature per class: \n", NB.theta_)
print("Variance of each feature per class: \n", NB.sigma_)

#predict the class for each data point
predicted = NB.predict(data)
print("Predictions:\n",np.array([predicted]).T)

# predict the probability/likelihood of the prediction
prob_of_pred = NB.predict_proba(data)
print("Probability of each class for the prediction: \n",prob_of_pred)

print("Accuracy of the model: ",NB.score(data,CV))

print("The confusion matrix:\n", metrics.confusion_matrix(CV, predicted, ['High','Low', 'Medium']))

# Calculating 5 fold cross validation results
model = GaussianNB()
kf = KFold(len(CV), n_folds=5)
scores = cross_val_score(model, data, CV, cv=kf)
print("MSE of every fold in 5 fold cross validation: ", abs(scores))

print("Does he have a high mental health, if he listens to 0.80 danceability and energy ", NB.predict([0.1,0.8]),NB.predict_proba([0.1,0.8]))