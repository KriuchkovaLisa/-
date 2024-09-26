#with open("input.txt", "r") as f:
#    text = f.read()
text = str(input().split())
#znak = ['.', '!', '?']
#for k in range(len(text)-1):
#    for i in range(len(znak)-1):
#        if text[]
s = text.count('.') + text.count('?') + text.count('!') - 2*text.count('...') - text.count('?!')
print(s)
    
