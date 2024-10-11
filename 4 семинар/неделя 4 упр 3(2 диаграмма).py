import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv') 

dk = list(df['PetalLengthCm'])
d=0
f=0
h=0
for i in range(len(list(df['PetalLengthCm']))):
    if dk[i] > 1.5:
        d+=1
    if dk[i] > 1.2 and dk[i] < 1.5:
        f+=1
    if dk[i] < 1.2:
        h+=1
plt.pie([d, f, h], labels = ['больше 1.5','больше 1.2см и меньше 1.5см','меньше 1.2см'])

plt.title('доля лепестков разной длины')

plt.show()
