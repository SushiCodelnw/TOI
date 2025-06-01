n = int(input())

for i in range(n):
    for j in range(i+1):
        if j!=0 and j!=n-1 and j!=i and i>=1 and i!=n-1:
            print("1",end=" ")
        else:
            print("0",end = " ")
    print()