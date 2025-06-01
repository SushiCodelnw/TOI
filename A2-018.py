c, n = map(str, input().split())

ss = {"R":0,"G":1,"B":2}
s = ss[c]

for i in range(int(n)):
    if s == 0:
        print("Red", end=" ")
    elif s == 1:
        print("Green", end=" ")
    elif s == 2:
        print("Blue", end=" ")
    s += 1
    if s> 2:
        s = 0
