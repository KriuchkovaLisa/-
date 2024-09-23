A = list(map(int, input().split()))
q = 1
for i in range (len(A)):
    q = q * (A[i]**(1/len(A)))
print(q)