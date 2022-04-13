from sys import stdin, stdout
n  = int(stdin.readline().strip())
flist = []
a = 1
for i in range(n):
    d = int(stdin.readline().strip())
    com = []
    for i in range(d):
        list_row = list(map(int, stdin.readline().strip().split()))
        flist.append(list_row)
    for i in flist:
        if (i[1]-i[0]) >= 120 and (i[1]-i[0]) <= 240:
            com.append("C")
        if i[1]-i[0] > 240 and i[1]-i[0] <=1440 and i[1]-i[0] >720:
            com.append("IMPOSSIBLE")
            break
        if i[1]-i[0] <= 60 and i[1]-i[0] >0:
            com.append("J")
        if i[1]-i[0] < 120 and i[1]-i[0] >60:
            com.append("C")
        if i[1]-i[0] == 720:
            com.append("C")
    com = "".join(com)
    print("Case #{}: {}".format(a,com))
    a +=1
    flist = []
    com = []