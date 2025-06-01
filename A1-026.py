e,o = 0,0


for i in range(3):
    if int(input()) % 2 == 0:
        e += 1
    else:
        o += 1

print("even", e)
print("odd", o)