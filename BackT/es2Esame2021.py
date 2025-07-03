def es(n,sol=[],c1 = 0,c2 = 0):
    if len(sol) == 2*n:
        print("".join(sol))
        return
    if len(sol)<n:
        sol.append("1")
        es(n,sol,c1+1,c2)
        sol.pop()
        sol.append("0")
        es(n,sol,c1,c2)
        sol.pop()

    if len(sol) >= n:
        s = 2*n - len(sol)
        if s-1 >= c1-c2:
            sol.append("0")
            es(n,sol,c1,c2)
            sol.pop()
        if c2 < c1:
            sol.append("1")
            es(n,sol,c1,c2+1)
            sol.pop()

es(2)