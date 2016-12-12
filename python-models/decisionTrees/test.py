import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import preprocessing
from sklearn.cross_validation import KFold, cross_val_score

dataset = pd.read_csv('data_decision2.csv')
print(dataset)

# prepare datasets to be fed in the regression model
#predict attend class given extra hours and grade
CV = dataset.health_categorical.reshape((len(dataset.health_categorical), 1))
data = (dataset.ix[:,'tempo':'popularity':'energy'].values).reshape((len(dataset.health_categorical), 3))

print(data)
print(CV)

# Create linear regression object
#
DT = DecisionTreeClassifier(criterion="entropy", min_samples_leaf = 3)

# Train the model using the training sets
DT.fit(data, CV)

# the model
with open("predict_attend_class.dot", 'w') as f:
    f = tree.export_graphviz(DT, out_file=f, feature_names=["tempo", "popularity", "energy"], class_names=["High-Health","Low-Health", "Medium-Health"], filled=True)


#predict the class for each data point
predicted = DT.predict(data)
print("Predictions: \n", np.array([predicted]).T)

# predict the probability/likelihood of the prediction
print("Probability of prediction: \n",DT.predict_proba(data))

print("Feature importance: ", DT.feature_importances_)

print("Accuracy score for the model: \n", DT.score(data,CV))

print(metrics.confusion_matrix(CV, predicted, labels=["High-Health","Medium-Health", "Low-Health"]))

# Calculating 5 fold cross validation results
model = DecisionTreeClassifier()
kf = KFold(len(CV), n_folds=5)
scores = cross_val_score(model, data, CV, cv=kf)
print("MSE of every fold in 5 fold cross validation: ", abs(scores))
print("Mean of the 5 fold cross-validation: %0.2f" % abs(scores.mean()))

#print("Does he attend class, if he gets 60 after putting 100 hours of effort: ", DT.predict([100,60]),DT.predict_proba([100,60]))
