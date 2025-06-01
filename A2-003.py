n = int(input())
l = list(map(int, input().split()))
d = 0

for i in range(n):
    if i == 0:
        if l[i] > l[i+1]:
            d += 1
    elif i == n-1:
        if l[i] > l[i-1]:
            d += 1
    else:
        if l[i] > l[i-1] and l[i] > l[i+1]:
            d += 1
print(d)