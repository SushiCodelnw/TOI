L, N = map(int, input().split())

layers = [i * i for i in range(L, 0, -1)] 

remaining = []

for count in layers:
    if N >= count:
        N -= count 
    else:
        remaining.append(count - N) 
        N = 0
        remaining += layers[layers.index(count)+1:] 
        break

print(len(remaining))
