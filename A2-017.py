c, s = map(str, input().split())

n = input().split()
cc = {
    "S":{"R":60,"T":80},
    "M":{"R":80,"T":100},
    "L":{"R":100,"T":120}
}
if n[0] == "N":
    print(cc[c][s])
else:
    nn = {
        "P":int(n[1])*15,
        "E":int(n[1])*10
    }
    print(cc[c][s] + nn[n[0]])