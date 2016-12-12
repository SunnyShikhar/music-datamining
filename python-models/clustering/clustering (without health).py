from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

dataset = pd.read_csv('data_all_norm_RFE.csv')
print(dataset)

KM = KMeans(n_clusters=2, init='k-means++', random_state=170)

KM = KM.fit(dataset)

print("The cluster centroids are: \n", KM.cluster_centers_)
print("Cluster", KM.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM.inertia_)

KM3 = KMeans(n_clusters=3, init='k-means++', random_state=170)

KM3 = KM3.fit(dataset)

print("The cluster centroids are: \n", KM3.cluster_centers_)
print("Cluster", KM3.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM3.inertia_)

KM4 = KMeans(n_clusters=4, init='k-means++', random_state=170)

KM4 = KM4.fit(dataset)

print("The cluster centroids are: \n", KM4.cluster_centers_)
print("Cluster", KM4.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM4.inertia_)

KM5 = KMeans(n_clusters=5, init='k-means++', random_state=170)

KM5 = KM5.fit(dataset)

print("The cluster centroids are: \n", KM5.cluster_centers_)
print("Cluster", KM5.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM5.inertia_)

KM6 = KMeans(n_clusters=6, init='k-means++', random_state=170)

KM6 = KM6.fit(dataset)

print("The cluster centroids are: \n", KM6.cluster_centers_)
print("Cluster", KM6.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM6.inertia_)

KM7 = KMeans(n_clusters=7, init='k-means++', random_state=170)

KM7 = KM7.fit(dataset)

print("The cluster centroids are: \n", KM7.cluster_centers_)
print("Cluster", KM7.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM7.inertia_)

KM8 = KMeans(n_clusters=8, init='k-means++', random_state=170)

KM8 = KM8.fit(dataset)

print("The cluster centroids are: \n", KM8.cluster_centers_)
print("Cluster", KM8.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM8.inertia_)

KM9 = KMeans(n_clusters=9, init='k-means++', random_state=170)

KM9 = KM9.fit(dataset)

print("The cluster centroids are: \n", KM9.cluster_centers_)
print("Cluster", KM9.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM9.inertia_)

KM10 = KMeans(n_clusters=10, init='k-means++', random_state=170)

KM10 = KM10.fit(dataset)

print("The cluster centroids are: \n", KM10.cluster_centers_)
print("Cluster", KM10.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM10.inertia_)

KM11 = KMeans(n_clusters=11, init='k-means++', random_state=170)

KM11 = KM11.fit(dataset)

print("The cluster centroids are: \n", KM11.cluster_centers_)
print("Cluster", KM11.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM11.inertia_)

KM12 = KMeans(n_clusters=12, init='k-means++', random_state=170)

KM12 = KM12.fit(dataset)

print("The cluster centroids are: \n", KM12.cluster_centers_)
print("Cluster", KM12.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM12.inertia_)

KM13 = KMeans(n_clusters=13, init='k-means++', random_state=170)

KM13 = KM13.fit(dataset)

print("The cluster centroids are: \n", KM13.cluster_centers_)
print("Cluster", KM13.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM13.inertia_)

KM14 = KMeans(n_clusters=14, init='k-means++', random_state=170)

KM14 = KM14.fit(dataset)

print("The cluster centroids are: \n", KM14.cluster_centers_)
print("Cluster", KM14.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM14.inertia_)

KM15 = KMeans(n_clusters=15, init='k-means++', random_state=170)

KM15 = KM15.fit(dataset)

print("The cluster centroids are: \n", KM15.cluster_centers_)
print("Cluster", KM15.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM15.inertia_)
#
colors = ['blue','yellow', 'green', 'red'] #'black']

def Tempo(y_data, y_name):
    plt.scatter(dataset.tempo, y_data, c=KM4.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
    plt.xlabel('tempo')
    plt.ylabel(y_name)
    plt.show()
Tempo(dataset.popularity, 'popularity');
Tempo(dataset.valence, 'valence');
Tempo(dataset.energy, 'energy');
Tempo(dataset.dance, 'dance');
# Tempo(dataset.acoustic, 'acoustic');
# Tempo(dataset.instrumental, 'instrumental');
# Tempo(dataset.liveness, 'liveness');
# #
def Popularity(y_data, y_name):
    plt.scatter(dataset.popularity, y_data, c=KM4.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
    plt.xlabel('popularity')
    plt.ylabel(y_name)
    plt.show()
Popularity(dataset.valence, 'valence');
Popularity(dataset.energy, 'energy');
Popularity(dataset.dance, 'dance');
# Popularity(dataset.acoustic, 'acoustic');
# Popularity(dataset.instrumental, 'instrumental');
# Popularity(dataset.liveness, 'liveness');

def Valence(y_data, y_name):
    plt.scatter(dataset.valence, y_data, c=KM4.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
    plt.xlabel('valence')
    plt.ylabel(y_name)
    plt.show()
Valence(dataset.energy, 'energy');
Valence(dataset.dance, 'dance');
# Valence(dataset.acoustic, 'acoustic');
# Valence(dataset.instrumental, 'instrumental');
#
def Energy(y_data, y_name):
    plt.scatter(dataset.energy, y_data, c=KM4.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
    plt.xlabel('energy')
    plt.ylabel(y_name)
    plt.show()
Energy(dataset.dance, 'dance');
# Energy(dataset.acoustic, 'acoustic');
# Energy(dataset.instrumental, 'instrumental');

# def Dance(y_data, y_name):
#     plt.scatter(dataset.dance, y_data, c=KM4.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
#     plt.xlabel('dance')
#     plt.ylabel(y_name)
#     plt.show()
# Dance(dataset.acoustic, 'acoustic');
# Dance(dataset.instrumental, 'instrumental');

# def Acoustic(y_data, y_name):
#     plt.scatter(dataset.acoustic, y_data, c=KM5.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
#     plt.xlabel('acoustic')
#     plt.ylabel(y_name)
#     plt.show()
# Acoustic(dataset.instrumental, 'instrumental');

# def Tempo3D(x_name, x_data, y_name, y_data):
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     ax.scatter(x_data, y_data,dataset.tempo,  c=KM.labels_, s=75)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()
# Tempo3D('popularity', dataset.popularity, 'valence', dataset.valence);
# Tempo3D('popularity', dataset.popularity, 'energy', dataset.energy);
# Tempo3D('popularity', dataset.popularity, 'dance', dataset.dance);
# Tempo3D('popularity', dataset.popularity, 'acoustic', dataset.acoustic);
# Tempo3D('popularity', dataset.popularity, 'instrumental', dataset.instrumental);
# Tempo3D('valence', dataset.valence, 'energy', dataset.energy);
# Tempo3D('valence', dataset.valence, 'dance', dataset.dance);
# Tempo3D('valence', dataset.valence, 'acoustic', dataset.acoustic);
# Tempo3D('valence', dataset.valence, 'instrumental', dataset.instrumental);
# Tempo3D('energy', dataset.energy, 'dance', dataset.dance);
# Tempo3D('energy', dataset.energy, 'acoustic', dataset.acoustic);
# Tempo3D('energy', dataset.energy, 'instrumental', dataset.instrumental);
# Tempo3D('dance', dataset.dance, 'acoustic', dataset.acoustic);
# Tempo3D('dance', dataset.dance, 'instrumental', dataset.instrumental);
# Tempo3D('acoustic', dataset.acoustic, 'instrumental', dataset.instrumental);
#
# def Popularity3D(x_name, x_data, y_name, y_data):
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     ax.scatter(x_data, y_data,dataset.popularity,  c=KM.labels_, s=75)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()
# Popularity3D('valence', dataset.valence, 'energy', dataset.energy);
# Popularity3D('valence', dataset.valence, 'dance', dataset.dance);
# Popularity3D('valence', dataset.valence, 'acoustic', dataset.acoustic);
# Popularity3D('valence', dataset.valence, 'instrumental', dataset.instrumental);
# Popularity3D('energy', dataset.energy, 'dance', dataset.dance);
# Popularity3D('energy', dataset.energy, 'acoustic', dataset.acoustic);
# Popularity3D('energy', dataset.energy, 'instrumental', dataset.instrumental);
# Popularity3D('dance', dataset.dance, 'acoustic', dataset.acoustic);
# Popularity3D('dance', dataset.dance, 'instrumental', dataset.instrumental);
# Popularity3D('acoustic', dataset.acoustic, 'instrumental', dataset.instrumental);
#
# def Valence3D(x_name, x_data, y_name, y_data):
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     ax.scatter(x_data, y_data,dataset.valence,  c=KM.labels_, s=75)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()
# Valence3D('energy', dataset.energy, 'dance', dataset.dance);
# Valence3D('energy', dataset.energy, 'acoustic', dataset.acoustic);
# Valence3D('energy', dataset.energy, 'instrumental', dataset.instrumental);
# Valence3D('dance', dataset.dance, 'acoustic', dataset.acoustic);
# Valence3D('dance', dataset.dance, 'instrumental', dataset.instrumental);
# Valence3D('acoustic', dataset.acoustic, 'instrumental', dataset.instrumental);
#
# def Energy3D(x_name, x_data, y_name, y_data):
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     ax.scatter(x_data, y_data,dataset.energy,  c=KM.labels_, s=75)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()
# Energy3D('dance', dataset.dance, 'acoustic', dataset.acoustic);
# Energy3D('dance', dataset.dance, 'instrumental', dataset.instrumental);
# Energy3D('acoustic', dataset.acoustic, 'instrumental', dataset.instrumental);
#
# def Dance3D(x_name, x_data, y_name, y_data):
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     ax.scatter(x_data, y_data,dataset.dance,  c=KM.labels_, s=75)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()
# Dance3D('acoustic', dataset.acoustic, 'instrumental', dataset.instrumental);







# fig = plt.figure(1, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
# ax.scatter(dataset.tempo, dataset.valence, dataset.health, c=KM.labels_, s=75)
# plt.xlabel('tempo')
# plt.ylabel('valence')
# plt.show()

# plt.scatter(dataset.tempo, dataset.valence, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
# plt.xlabel('tempo')
# plt.ylabel('valence')
# plt.show()
#
# plt.scatter(dataset.tempo, dataset.energy, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
# plt.xlabel('tempo')
# plt.ylabel('energy')
# plt.show()
#
# plt.scatter(dataset.tempo, dataset.dance, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
# plt.xlabel('tempo')
# plt.ylabel('dance')
# plt.show()
#
# plt.scatter(dataset.tempo, dataset.acoustic, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
# plt.xlabel('tempo')
# plt.ylabel('acoustic')
# plt.show()
#
# plt.scatter(dataset.tempo, dataset.instrumental, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
# plt.xlabel('tempo')
# plt.ylabel('instrumental')
# plt.show()