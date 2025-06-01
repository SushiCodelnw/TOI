l = int(input())

a = input()
b = input()

x = 0
for i in range(l):
    if not int(a[i]) + int(b[i]) == 9:
        x += 1
if x == 0:
    print("YES")
else:
    print("NO", x)