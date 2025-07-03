def ex4(M):
    n = len(M[0])
    T = [[0 for k in range(n)] for _ in range(n)]
    matrice_max = 0
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                if i == 0 or j == 0:
                    T[i][j] = M[i][j]
                else:
                    T[i][j] = 1+ min(T[i-1][j],T[i][j-1], T[i-1][j-1])
            if T[i][j] > matrice_max:
                matrice_max = T[i][j]
    return matrice_max

M = [[1,0,1,1,1],
     [1,1,1,1,1],
     [1,1,1,0,1],
     [1,1,1,1,1],
     [1,1,0,1,1]]

print(ex4(M))