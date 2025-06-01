mylist = []

for i in range(3):
    mylist.append(int(input()))

max_mylist = sorted(mylist,reverse=True)
min_mylist = sorted(mylist)

def r():
    if len(set(mylist)) != len(mylist):
        return "neither"
    elif max_mylist == mylist:
        return "decreasing"
    elif min_mylist == mylist:
        return "increasing"
    else:
        return "neither"
    
print (r())