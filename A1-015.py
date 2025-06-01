n = input()
l = input()
a = input()

if (len(n) >= 5 or len(l) >= 5):
    print(n[0] + n[1] + l[len(l) - 1] + a[len(a) - 1])
else:
    print(n[0] + a + l[len(a) - 1])