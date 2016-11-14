import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('InputTraumatic.csv')
print(dataset)

plt.figure(1)
plt.scatter(dataset.tempo, dataset.health, color='blue')
plt.title('Mental health as a function of song tempo')
plt.xlabel('tempo')
plt.ylabel('health')
plt.show()

plt.figure(2)
plt.scatter(dataset.tempo, dataset.enjoy_life, color='blue')
plt.title('Ability to enjoy life as a function of song tempo')
plt.xlabel('tempo')
plt.ylabel('ability to enjoy life')
plt.show()

plt.figure(1)
plt.scatter(dataset.valence, dataset.health, color='blue')
plt.title('Mental health as a function of song valence')
plt.xlabel('valence')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(dataset.liveness, dataset.health, color='blue')
plt.title('Mental health as a function of song liveness')
plt.xlabel('liveness')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(dataset.energy, dataset.health, color='blue')
plt.title('Mental health as a function of song energy')
plt.xlabel('energy')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(dataset.dance, dataset.health, color='blue')
plt.title('Mental health as a function of song dance level')
plt.xlabel('dance level')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(dataset.acoustic, dataset.health, color='blue')
plt.title('Mental health as a function of song acoustic level')
plt.xlabel('acoustic level')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(dataset.instrumental, dataset.health, color='blue')
plt.title('Mental health as a function of song instrumentalness')
plt.xlabel('instrumentalness')
plt.ylabel('health')
plt.show()

#tempo = dataset.tempo.reshape((len(dataset.tempo), 1))
#health = dataset.health.reshape((len(dataset.health), 1))

#regr = linear_model.LinearRegression()

#regr.fit(tempo, health)

#predicted_results = regr.predict(tempo)

#plt.plot(tempo, predicted_results, color='green', linewidth=3)
#plt.scatter(tempo, health, color='black')
#plt.xlabel("tempo")
#plt.ylabel("health")
#plt.show()