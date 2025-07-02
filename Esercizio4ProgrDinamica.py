def ex4(M):
    n = len(M[0])
    T = [[0 for k in range(n)] for _ in range(n)]
    T[0] = M[0]
    for x in range(n):
        for y in range(n):
            T[x][0] = M[x][0]


    for i in range(n):
        for j in range(n):
            if

M = [[1,0,1,1,1],
     [1,1,1,1,1],
     [1,1,1,0,1],
     [1,1,1,1,1],
     [1,1,0,1,1]]