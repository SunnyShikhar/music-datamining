import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import pylab as P
import seaborn as sns

from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

#This is a function that will plot a histogram based on the data field provided
def PlotHistogram(dataOnX, XName):
    plt.figure(1)
    plt.hist(dataOnX)
    plt.xlabel(XName)
    plt.show()

#This is a function that will make bar charts for any of the categorical variables
def PlotBarChart(CategoricalVar, data, XName):
    sns.countplot(CategoricalVar, data=data)
    plt.xlabel(XName)
    plt.show()


def PlotScatter(dataOnY, dataOnX, YName, XName):
    plt.figure(1)
    plt.scatter(dataOnY, dataOnX, color='blue')
    plt.title('Mental health as a function of song tempo')
    plt.xlabel(YName)
    plt.ylabel(XName)
    plt.show()

dataset = pd.read_csv('data_all.csv')

#Plots all the histograms for the song attributes
PlotHistogram(dataset.tempo, 'tempo')
#PlotHistogram(dataset.liveness, 'liveness')
PlotHistogram(dataset.valence, 'valence')
PlotHistogram(dataset.dance, 'dance')
#PlotHistogram(dataset.acoustic, 'acoustic')
#PlotHistogram(dataset.instrumental, 'instrumental')
PlotHistogram(dataset.energy, 'energy')

PlotBarChart(dataset.health_categorical, dataset, 'Mental Health')
PlotBarChart(dataset.gender, dataset, 'gender')
PlotBarChart(dataset.age_range, dataset, 'age range')
PlotBarChart(dataset.traumatic_experience, dataset, 'Trauma')
PlotBarChart(dataset.hours_of_music_categorical, dataset, 'Hours of Music')
PlotBarChart(dataset.tempo_categorical, dataset, 'tempo')
PlotBarChart(dataset.valence_categorical, dataset, 'valence')
PlotBarChart(dataset.dance_categorical, dataset, 'dance')
PlotBarChart(dataset.energy_categorical, dataset, 'energy')