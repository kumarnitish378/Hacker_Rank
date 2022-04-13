T = 3
N = 4
while (T > 0):
    data = [[1,2,3,4],
            [2,1,4,3],
            [3,4,1,2],
            [4,3,2,1]]
    # data = [[2, 5, 2, 2],
    #         [5, 3, 2, 3],
    #         [2, 2, 2, 3],
    #         [2, 2, 2, 2]]
    def d_sum (data):
        k =[]
        for i in range (len(data)):
            for j in range (len(data)):
                if i == j:
                    k.append(data[i][j])
        s = 0
        for i in k:
            s = s+i
        return s

    def row(data):
        c = 0
        r = 0
        for i in

        return r
    def col(data):
        pass
    print("case #"+str(1)+": ", row(data))
    break