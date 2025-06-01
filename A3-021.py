n, k = map(int, input().split())

a = [int(input()) / k for _ in range(n)]

base = min(a)
count = sum(1 for i in a if i >= base)
print(count)