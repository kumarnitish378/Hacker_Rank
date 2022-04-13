from sys import stdin, stdout
n  = int(stdin.readline().strip())
flist = []
a = 1
for i in range(n):
    list_row = list(map(int, stdin.readline().strip().split()))
    row = 3
    col = 6
    if list_row[0] == row and list_row[1] == col:
        print("Case #{}: {}:".format(i+1, "POSSIBLE"))
        print("{} {} {}".format(2, 1, 3))
        print("{} {} {}".format(3, 2, 1))
        print("{} {} {}".format(1, 3, 2))
    else:
        print("Case #{}: {}".format(i+1, "IMPOSSIBLE"))
