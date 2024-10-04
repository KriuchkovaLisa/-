import numpy as np
x = np.array([4,5,6,3,4,6,3,5,4,3,5,2,4,5,3,3])
y = np.array([8,9,7,8,9,7,9,8,9,7,8,7,9,6,7,5])
Xm = sum(x)/len(x) 
Ym = sum(y)/len(y) 
xy = x*y
XYm = sum(xy)/len(xy)
x2 = x*x
X2m = sum(x2)/len(x2)
b = (XYm - Xm*Ym)/(X2m - Xm*Xm)
a = Ym - b*Xm
print('y = ', round(a,3), 'x + ', round(b,3), sep = '')