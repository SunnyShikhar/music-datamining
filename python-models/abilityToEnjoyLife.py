import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

dataset = pd.read_excel('data-files/master-data.xlsx')
print(dataset)

plt.figure(1)
plt.scatter(dataset.dancability, dataset.enjoy_life, color='blue')
plt.title('Ability to enjoy life vs. Dancability')
plt.xlabel('dancability')
plt.ylabel('ability to enjoy life')
plt.show()

plt.figure(2)
plt.scatter(dataset.energy, dataset.enjoy_life, color='blue')
plt.title('Ability to enjoy life vs. Energy')
plt.xlabel('energy')
plt.ylabel('ability to enjoy life')
plt.show()

plt.figure(3)
plt.scatter(dataset.bpm, dataset.enjoy_life, color='blue')
plt.title('Ability to enjoy life vs. bpm')
plt.xlabel('bpm')
plt.ylabel('ability to enjoy life')
plt.show()

plt.figure(4)
plt.scatter(dataset.valence, dataset.enjoy_life, color='blue')
plt.title('Ability to enjoy life vs. valence')
plt.xlabel('valence')
plt.ylabel('ability to enjoy life')
plt.show()