import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def PlotHistogram(dataOnX, XName):
    plt.hist(dataOnX.dropna())
    plt.xlabel(XName)
    plt.title(XName + ' Histogram')
    plt.show()

def PlotBarChart(CategoricalVar, data, XName):
    sns.countplot(CategoricalVar, data=data)
    plt.xlabel(XName)
    plt.title( XName + ' Bar Chart')
    plt.show()

def PlotScatter(dataOnY, dataOnX, YName, XName):
    plt.scatter(dataOnX, dataOnY, color='blue')
    plt.title(YName + ' as a function of ' + XName)
    plt.xlabel(YName)
    plt.ylabel(XName)
    plt.show()
    
def MultiScatter(dataOnY, x1, x2, x1Name, x2Name, Yname):
    plt.scatter(x1, dataOnY, color='blue')
    plt.scatter(x2, dataOnY, color='red')
    plt.title(Yname + " vs " + x1Name + ' & ' + x2Name)
    plt.xlabel(x1Name + ' in blue, '+ x2Name + ' in red')
    plt.ylabel(Yname)
    plt.show()

dataset = pd.read_csv('data/master.csv')

#Plots all the histograms for the song attributes
PlotHistogram(dataset.tempo, 'tempo')
PlotHistogram(dataset.liveness, 'liveness')
PlotHistogram(dataset.valence, 'valence')
PlotHistogram(dataset.dance, 'dance')
PlotHistogram(dataset.acoustic, 'acoustic')
PlotHistogram(dataset.instrumental, 'instrumental')
PlotHistogram(dataset.popularity, 'popularity')
PlotHistogram(dataset.liveness, 'liveness')
PlotHistogram(dataset.acoustic, 'acousticness')
PlotHistogram(dataset.instrumental, 'instrument')

# Plot mental health and target value histogram
PlotHistogram(dataset.total_health, 'total mental health')
PlotHistogram(dataset.life_enjoyment, 'Ability to Enjoy Life')
PlotHistogram(dataset.resilience, 'Resiliency')
PlotHistogram(dataset.balanced_life, 'Ability to Live A Balanced Lifestyle')
PlotHistogram(dataset.emotional_flex, 'Emotional Flexibility')
PlotHistogram(dataset.self_actualization, 'Self Actualization/Awareness')

# Plot categorical variable counts
PlotBarChart(dataset.health_categorical, dataset, 'Mental Health')
PlotBarChart(dataset.gender, dataset, 'gender')
PlotBarChart(dataset.age, dataset, 'age range')
PlotBarChart(dataset.trauma, dataset, 'Trauma')
PlotBarChart(dataset.amount_music, dataset, 'Hours of Music')

# Plot song attributes against mental health totals
PlotScatter(dataset.total_health, dataset.tempo, 'Mental Health', 'Tempo')
PlotScatter(dataset.total_health, dataset.energy, 'Mental Health', 'Energy')
PlotScatter(dataset.total_health, dataset.dance, 'Mental Health', 'Danceability')
PlotScatter(dataset.total_health, dataset.popularity, 'Mental Health', 'Popularity')
PlotScatter(dataset.total_health, dataset.liveness, 'Mental Health', 'Liveness')
PlotScatter(dataset.total_health, dataset.acoustic, 'Mental Health', 'Acoustic')
PlotScatter(dataset.total_health, dataset.instrumental, 'Mental Health', 'Instrumentalness')

#Compare multiple attributes
MultiScatter(dataset.total_health, dataset.dance, dataset.energy, 'Dance', 'Energy', 'Mental Health')
MultiScatter(dataset.total_health, dataset.instrumental, dataset.acoustic, 'Instrumental', 'Acoustic', 'Mental Health')
MultiScatter(dataset.total_health, dataset.popularity, dataset.liveness, 'Popularity', 'Liveness', 'Mental Health')