def es1(n,sol=[],ca = 0):
    if len(sol) == n:
        print("".join(sol))
        return
    if len(sol)+2 <= n and ca%2 == 0:
        sol.append("a")
        sol.append("a")
        es1(n,sol,ca+2)
        sol.pop()
        sol.pop()
    sol.append("b")
    es1(n,sol,ca)
    sol.pop()

es1(5)