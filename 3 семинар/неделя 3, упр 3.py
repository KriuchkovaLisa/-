a = int(input())
b = int(input())
#ax + by = d
#d = НОД(a,b)
s = a
l =[]
for k in range(2, a):
    while (s%k == 0):
        l.append(k)
        s = s//k
g = []
s = b
for k in range(2, b):
    while (s%k == 0):
        g.append(k)
        s = s//k
h = []
for i in range(len(l)):
    if l[i] in g:
        h.append(l[i])
if len(h)<1:
    h.append(1)
d = max(h)
if len(h)<1:
    d = 1
x = 0
y = 0
r = 0
while r != 1:
    x +=1
    y = 0
    while y != x:
        y +=1
        if ((x*a + y*b)==d):
            print(x, y, d)
            r = 1
        if ((-x*a + y*b)==d):
            print(-x, y, d)
            r = 1
        if ((-x*a - y*b)==d):
            print(-x, -y, d)
            r = 1
        if ((x*a - y*b)==d):
            print(x, -y, d)
            r = 1
    if r == 1:
        break
    