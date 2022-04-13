from sys import stdin, stdout
n  = int(stdin.readline().strip())
flist = []
a = 1
for i in range(n):
    data = stdin.readline()
    lst =[]
    temp =[]
    out = []
    for i in range(len(data)-1):
        lst.append(int(data[i]))
        temp.append(int(data[i]))
    temp.sort()
    for i in range(len(lst)):
        po = 0
        if lst[i]<temp[-1] and lst[i] > 0:
            while temp[-1] - lst[i] != 0:
                out.append("(")
                po +=1
        out.append(lst[i])
        if po > 0:
            while po > 0:
                out.append(")")
                po -= 1

    print(out)
    #print("Case #{}: {}".format(a, data))
    #a +=1
    break