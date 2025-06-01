n, m = map(int, input().split())

f_list, s_list, e_list, o_list = [], [], [], []

for _ in range(n):
    f_list.append(input().split(" "))
    
e_list = [row[:] for row in f_list]


for i in range(n - 1):
    for j in range(m):
        if f_list[i][j] == "*":
            e_list[i + 1][j] = "*"
            e_list[i][j] = "*"
        else:
            e_list[i + 1][j] = "-"
            e_list[i][j] = "-"

for row in e_list:
    print(" ".join(row))

            