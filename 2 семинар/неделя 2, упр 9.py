with open("input.txt", "r") as f:
    text = f.read()
s = text.count('.') + text.count('?') + text.count('!') - 2*text.count('...') - text.count('?!')
print(s)
    
