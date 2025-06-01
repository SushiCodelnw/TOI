a = [int(input()) for _ in range(int(input()))]

l, s = [],[]

for i in a:
    if i > 18:
        l.append(i)
    else:
        s.append(i)

d = 0

for j in range(len(l)):
    d += 1
    if s:
        s.pop()
    if not j == len(l) -1 and not s:
        d += 1
d += len(s)

print(d)