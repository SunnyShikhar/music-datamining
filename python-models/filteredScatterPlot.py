import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('data-files/data_all.csv')
print(dataset)

filter2 = dataset[dataset['gender'] == 'Male']
#filter2 = dataset[dataset['hours_of_music'] == '2+ hours']

plt.figure(1)
plt.scatter(filter2.tempo, filter2.health, color='blue')
plt.title('Mental health as a function of song tempo')
plt.xlabel('tempo')
plt.ylabel('health')
plt.show()

# plt.figure(2)
# plt.scatter(dataset.tempo, dataset.enjoy_life, color='blue')
# plt.title('Ability to enjoy life as a function of song tempo')
# plt.xlabel('tempo')
# plt.ylabel('ability to enjoy life')
# plt.show()

plt.figure(1)
plt.scatter(filter2.valence, filter2.health, color='blue')
plt.scatter(filter2.liveness, filter2.health, color='red')
plt.title('Mental health as a function of song valence')
plt.xlabel('valence in blue, liveness in red')
plt.ylabel('health')
plt.show()

plt.figure(1)
plt.scatter(filter2.energy, filter2.health, color='blue')
#plt.scatter(filter2.dance, filter2.health, color='red')
plt.title('Mental health as a function of song energy')
plt.xlabel('energy in blue, dance in red')
plt.ylabel('health')
plt.show()