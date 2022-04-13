import time
p_t = time.time()
from Indicium import stdin, stdout
n  = int(stdin.readline().strip())
flist = []
for i in range(n):
    d = int(stdin.readline().strip())

    for i in range(d):
        list_row = list(map(int,stdin.readline().strip().split()))
        flist.append(list_row)
def d_sum(flist):
    k = 0
    for i in range(len(flist)):
        for j in range(len(flist)):
            if i == j:
                k = k+flist[i][j]
    return k

def row(flist):
    r = 0
    for i in flist:
        b = set(i)
        if (len(i) - len(b) > 0):
            if r <= len(i) - len(b):
                r = len(i) - len(b)+1
    return r
def col(flist):
    colon = 0
    c = []
    for i in range(len(flist)):
        for j in range(len(flist)):
            c.append(flist[j][i])
        b = set(c)
        if (len(c) - len(b) > 0):
            if colon <= len(c) - len(b):
                colon = len(c) - len(b)+1
        c = []
    return
print("case #"+str(1)+":", d_sum(flist), row(flist), col(flist))
