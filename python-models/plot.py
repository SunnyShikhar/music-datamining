import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('data_all.csv')
# print(dataset)

def MultiPlot(dataOnX, XName):	

	def plotGraph( dataOnY, dataOnX, YName, XName):
		plt.figure(1)
		plt.scatter(dataOnY, dataOnX, color='blue')
		plt.title('Mental health as a function of song tempo')
		plt.xlabel(YName)
		plt.ylabel(XName)
		plt.show()
	plotGraph(dataset.tempo, dataOnX, 'tempo', XName);
	plotGraph(dataset.liveness, dataOnX, 'liveness', XName);
	plotGraph(dataset.valence, dataOnX, 'valence', XName);
	plotGraph(dataset.energy, dataOnX, 'energy', XName);
	plotGraph(dataset.dance, dataOnX, 'dance', XName);
	plotGraph(dataset.acoustic, dataOnX, 'acoustic', XName);
	plotGraph(dataset.instrumental, dataOnX, 'instrumental', XName);

MultiPlot(dataset.enjoy_life, 'enjoy life');
MultiPlot(dataset.resilience, 'resilience');
MultiPlot(dataset.balanced, 'balanced');
MultiPlot(dataset.emotional_flexibility, 'emotional flexibility');
MultiPlot(dataset.self_actualization, 'self actualization');
MultiPlot(dataset.health, 'health');


