def es6(n,m,k,sol = [], rip = None):
    if len(sol) == n:
        print("".join(sol))
        return
    if rip is None:
        rip = [0] * (n+1)

    for i in range(1,m+1):
        if rip[i] < k:
            sol.append(str(i))
            rip[i] +=1
            es6(n,m,k,sol,rip)
            sol.pop()
            rip[i] -=1


es6(3,2,2)