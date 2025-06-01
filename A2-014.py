name1 = input().strip()
name2 = input().strip()

if len(name1) < len(name2):
    name1 += name1[0] * (len(name2) - len(name1))
elif len(name2) < len(name1):
    name2 += name2[0] * (len(name1) - len(name2))

symbols = []
for c1, c2 in zip(name1, name2):
    if c1.lower() in "love" or c2.lower() in "love":
        symbols.append("w")
    else:
        symbols.append("$")

yantra = ''.join(symbols)
w_count = yantra.count("w")

if w_count % 2 == 1: 
    max_w_streak = 0
    current = 0
    for char in yantra:
        if char == 'w':
            current += 1
            max_w_streak = max(max_w_streak, current)
        else:
            current = 0
    yantra += str(max_w_streak)
elif "ww" not in yantra: 
    yantra += "#"

print(yantra)
