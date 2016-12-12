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
#Song_info = dataset[dataset.position.isin(['dance_categorical', 'health'])]
fieldNames = [dataset.energy_categorical, dataset.dance_categorical, dataset.liveness_categorical, dataset.valence_categorical, dataset.tempo_categorical, dataset.instrumental_categorical, dataset.acoustic_categorical, dataset.popularity_categorical, dataset.gender, dataset.hours_of_music_categorical, dataset.traumatic_experience]
for Name in fieldNames:
	sns.swarmplot(x=Name, y=dataset.health, data=dataset)
	plt.show()