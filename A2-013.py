k, p = map(str, input().split())
s, w, cc = map(str, input().split())

kl = {
    "H":5,
    "O":3,
    "J":2
}
sl = {
    "R": {"1":12, "2":18, "3":25},
    "T": {"1":15, "2":20, "3":30},
    "M": {"1":10, "2":15, "3":20},
}

print((kl[k] * int(p)) + (sl[s][w] * int(cc)))