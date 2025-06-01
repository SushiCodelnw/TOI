a = int(input())

for i in range(a):
    if ((i + 1) % 5) == 0:
        print("X", end="")
    else:
        print("*", end="")