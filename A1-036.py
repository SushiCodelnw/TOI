n = int(input())

n -= n%10

while(True):
    print(n, end=" ")
    n -= 10
    if n < 0 : break