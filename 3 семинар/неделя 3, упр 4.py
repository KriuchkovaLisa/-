size = int(input())
b = str(input())
for i in range((size//2)+2):
    print(b*i)
for k in range((size - ((size//2)+1)), 0,-1):
    print(b*k)
    