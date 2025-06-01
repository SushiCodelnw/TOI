l = []

for i in range(3):
    l.append(input())
    
l = dict.fromkeys(l)

if len(l) == 1:
    print("all the same")
elif len(l) == 2:
    print("neither")
elif len(l) == 3:
    print("all different")

