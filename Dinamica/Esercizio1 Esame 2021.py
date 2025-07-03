def es(n,k):
    T =[[0]*(n+1) for x in range(k+1)]

    for i in range(1,k+1):
        for j in range(1,n+1):
            if j < i:
                continue
            elif i == j:
                T[i][j] = 1
            else:
                T[i][j] = T[i-1][j-1]+T[i][j-1]*i
    return T[-1][-1]


print(es(4,2))