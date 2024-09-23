N = input()
b = int(input())
c = int(input())
R = (int(N, b))
string = ''
while R > 0:
    string+=str(R%c)
    R//=c
print(string[::-1])