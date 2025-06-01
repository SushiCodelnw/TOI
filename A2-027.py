a = int(input())

l = []
for i in range(a):
    l.append(int(input()))

print(max(l))

x = 0
for i in l:
    if i == max(l):
        x +=1
        
print(x)