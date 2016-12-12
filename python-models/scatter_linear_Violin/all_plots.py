import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('data_all.csv')
print(dataset)

traumaDataset = dataset[dataset['traumatic_experience'] == 'Yes']
nonTraumaDataset = dataset[dataset['traumatic_experience'] == 'No']

plt.figure(1)
plt.scatter(traumaDataset.dance, traumaDataset.health, color= 'red', label='traumatic experience')
plt.scatter(nonTraumaDataset.dance, nonTraumaDataset.health, color = 'blue', label='non-traumatic experience')
plt.title('Mental health as a function of song danceability')
plt.xlabel('danceability')
plt.ylabel('health')
plt.legend()
plt.show()

plt.figure(2)
plt.scatter(dataset.tempo, dataset.health, color='blue')
plt.title('Mental Health as a function of song tempo')
plt.xlabel('tempo (bpm)')
plt.ylabel('health')
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