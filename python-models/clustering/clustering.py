from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

dataset = pd.read_csv('data_all_numerical.csv')
print(dataset)

KM = KMeans(n_clusters=3, init='k-means++', random_state=170)

KM = KM.fit(dataset)

print("The cluster centroids are: \n", KM.cluster_centers_)
print("Cluster", KM.labels_)
print("Sum of distances of samples to their closest cluster center: ", KM.inertia_)

colors = ['blue','yellow','green']

plt.scatter(dataset.tempo, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('tempo')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.liveness, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('liveness')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.valence, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('valence')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.energy, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('energy')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.dance, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('dance')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.acoustic, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('acoustic')
plt.ylabel('health')
plt.show()

plt.scatter(dataset.instrumental, dataset.health, c=KM.labels_, cmap=matplotlib.colors.ListedColormap(colors), s=75)
plt.xlabel('instrumental')
plt.ylabel('health')
plt.show()

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(dataset.tempo, dataset.dance, dataset.health, c=KM.labels_, s=75)
plt.xlabel('tempo')
plt.ylabel('dance')
plt.show()

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(dataset.tempo, dataset.valence, dataset.health, c=KM.labels_, s=75)
plt.xlabel('tempo')
plt.ylabel('valence')
plt.show()