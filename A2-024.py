l, p = map(int, input().split())
r, m, f = map(int, input().split())

k = []
for _ in range(p):
    k.append(list(map(int, input().split())))

def go(s):
    h = 0
    po = 0
    while(True):
        for a, b in k:
            if h == a:
                po += b
        h += s
        if h > l:
            break
    return po

rab, mon, fro = go(r),go(m),go(f)
li = [rab, mon, fro]

if max(li) == rab:
    print("Rabbit", rab)
if max(li) == mon:
    print("Monkey", mon)
if max(li) == fro:
    print("Frog", fro)

    