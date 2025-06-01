l = int(input())

aa, bb = "", "0"
x = 0
for i in range(l):
    a, b = map(str, input().split())
    if int(b) > 15:
        x += 1
    if int(b) > int(bb):
        aa,bb = a, b
        
print(x)
if not aa == "" and not bb == "0":
    print(aa,bb)