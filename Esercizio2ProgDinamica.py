def es2(n):
    T = [0 for _ in range(n+1)]
    if n == 0: return 1
    if n == 1: return 2
    if n == 2: return 4

    T[0] = 1
    T[1] = 2
    T[2] = 4
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2] +T[i-3]

    return T[n]
print(es2(4))