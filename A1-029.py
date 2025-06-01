a=input()

e = ["a", "e", "i", "o", "u"]
o = 0
for i in range(len(a)):
    if a[i].lower() in e:
        o += 1
        
print(o)