l = list(input().split())
a = int(l[0])
l = str(l[1])
n = len(l)//a
str = ''
for i in range(n):
    group = l[(i*n):((i+1)*n)]
    oborot = group[::-1]
    str += oborot
print(str)