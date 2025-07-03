def es1(n):
    T = [0 for i in range(n+1)]
    if n == 0: return 0
    if n == 1: return 2
    if n == 2: return 3
    T[0] = 1
    T[1] = 2
    for i in range(2,n+1):
        T[i] = T[i-1]+T[i-2]

    return T[n]

print(es1(5))

