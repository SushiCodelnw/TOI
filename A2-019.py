a = input()
max_u_count = 0
found_buu = False

i = 0
while i < len(a) - 2:
    if a[i].lower() == 'b' and a[i+1].lower() == 'u' and a[i+2].lower() == 'u':
        count = 0
        j = i + 1
        while j < len(a) and a[j].lower() == 'u':
            count += 1
            j += 1
        max_u_count = max(max_u_count, count)
        found_buu = True
        i = j
    else:
        i += 1

if found_buu:
    print("Yes", max_u_count)
else:
    if 'b' in a.lower():
        idx = next(i for i in range(len(a)) if a[i].lower() == 'b')
        result = a[:idx+1] + 'U' * (len(a) - idx - 1)
        print(result)
    else:
        pattern = "BUU"
        repeated = (pattern * ((len(a) + 2) // 3))[:len(a)]
        print(repeated)
