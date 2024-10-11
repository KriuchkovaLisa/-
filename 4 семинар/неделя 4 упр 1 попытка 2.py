import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (16,9)) 
ax1 = fig.add_subplot(111) 

x_measured = [0.3839, 0.4877, 0.6009, 0.7265, 0.8693, 1.0355, 1.4281]
y_measured = [1.0486, 1.98, 3.5115, 4.7218, 6.0818, 7.9751, 12.3959]
plt.xlabel('t, c')
plt.ylabel('a, m/c^2')

x = [0.3839, 1.4281]
y = np.interp(x, x_measured, y_measured)


ax1.scatter(x_measured, y_measured, marker='x')


ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.01, color = 'k', linestyle = 'None')


ax1.plot(x, y, 'r')
plt.plot(x,y,'r',label = 'a(t)')

ax1.grid()
plt.legend()
plt.show()