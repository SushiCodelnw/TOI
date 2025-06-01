l = [list(map(int, input().split())) for i in range(5)]

n = -1
t = -1
for i in range(5):
    if sum(l[i]) % 2 != 0:
        n = i
for i in range(5):
    if sum(l[j][i] for j in range(5)) % 2 != 0:
        t = i
print(n,t)