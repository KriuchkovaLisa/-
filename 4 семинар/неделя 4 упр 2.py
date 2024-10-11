import numpy as np
import matplotlib.pyplot as plt

pos = 0
scale = 10
size1 = 800
values1 = np.random.normal(pos, 10, size1)
plt.hist(values1, 20, label = 'гистограмма для 800 значений', alpha = .8 ,edgecolor = 'blue')
size2 = 500
values2 = np.random.normal(pos, 10, size2)
plt.hist(values2, 20, label = 'гистограмма для 500 значений', alpha = 0.6,  edgecolor = 'red')
size3 = 200
values3 = np.random.normal(pos, 10, size3)
plt.hist(values3, 20, label = 'гистограмма для 200 значений', alpha = 0.4 ,edgecolor = 'green')
plt.legend()

plt.show()
