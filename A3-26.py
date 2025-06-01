n1, n2 = map(int, input().split())

f_list, s_list, e_list = [], [], []
sybol = str()

for _ in range(n1):
    f_list.append(input())
for _ in range(n1):
    s_list.append(input())

for i in range(n1):
    for j in range(n2):
        if f_list[i][j] == "-" and s_list[i][j] == "-":
            e_list.append("-")
        elif (f_list[i][j] == "-" and s_list[i][j] == "+") or (f_list[i][j] == "+" and s_list[i][j] == "-"):
            e_list.append("+")
        elif (f_list[i][j] == "-" and s_list[i][j] == "x") or (f_list[i][j] == "x" and s_list[i][j] == "-"):
            e_list.append("x")
        elif (f_list[i][j] == "+" and s_list[i][j] == "x") or (f_list[i][j] == "x" and s_list[i][j] == "+"):
            e_list.append("*")

for i in range(n1):
    for j in range(n2):
        print(e_list[n2 * i + j], end="")
    print()