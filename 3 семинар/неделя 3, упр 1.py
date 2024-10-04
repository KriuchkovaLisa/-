n = int(input())
a = 1
b = 1
if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    for i in range (3,n):
        c = a + b
        a = b
        b = c
    print(b)

# 0 1 1 2 3 5 8 13 21 34 55