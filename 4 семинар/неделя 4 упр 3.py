import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv') 
dg = list(df['Species'])
a=0
b=0
c=0
for i in range(len(list(df['Species']))):
    if dg[i] == 'Iris-setosa':
        a+=1
    if dg[i] == 'Iris-versicolor':
        b+=1
    if dg[i] == 'Iris-virginica':
        c+=1
plt.pie([a, b, c], labels = ['setosa','versicolor','virginica'])

plt.title('доли разных видов')

plt.show()


