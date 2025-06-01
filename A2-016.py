n = input()
m = input()

if n[2] == m[2] and n[3] == m[3] and n[4] == m[4] and n[5] == m[5] and n[6] == m[6]:
    if n[0] == m[0]:
        print(1000000)
    else:
        print(100000)
elif n[4] == m[4] and n[5] == m[5] and n[6] == m[6]:
    if n[0] == m[0]:
        print(2000)
    else:
        print(200)
elif n[5] == m[5] and n[6] == m[6]:
    if n[0] == m[0]:
        print(1000)
    else:
        print(100)
elif n[0] == m[0]:
    print(20)
else:
    print(0)