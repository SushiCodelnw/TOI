text = input().strip().upper()

if all(c in 'IT' for c in text):
    print(f"unknown {len(text)}")
else:
    max_a_len = 0
    i = 0
    while i < len(text):
        c = text[i]

        if c == 'R':
            i += 1
            a_count = 0
            while i < len(text) and text[i] == 'A':
                a_count += 1
                i += 1
            if a_count == 0:
                print(f"no {i}")
                break
            max_a_len = max(max_a_len, a_count)

        elif c == 'A':
            print(f"no {i}")
            break

        elif c == 'B':
            i += 1
            if i >= len(text) or text[i] not in 'IT':
                print(f"no {i}")
                break
            while i < len(text) and text[i] in 'IT':
                i += 1

        elif c in 'IT':
            i += 1

        else:
            print(f"no {i}")
            break
    else:
        print(f"yes {max_a_len}")
