s = int(input())
a = s
for k in range(2, s):
    while (a%k == 0):
        print(k)
        a = a//k
    
