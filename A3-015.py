loop = int(input())
po = 0
va = 0
a = []
for i in range(loop):
    a.append(int(input()))
a.sort()
for i in a:
    va += i
    po += va*2
print(po)   