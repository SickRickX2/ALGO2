def es2(n, sol = [], ca = 0,cb = 0):
    if n%2 == 1: return
    if len(sol) == n:
        print("".join(sol))
        return
    if len(sol)+2 <= n:
        sol.append("a")
        es2(n,sol,ca+1,cb)
        sol.pop()
        sol.append("b")
        es2(n,sol,ca,cb+1)
        sol.pop()
    if (ca%2== 0 and cb %2 ==1):
        sol.append("a")
        es2(n,sol,ca+1,cb)
        sol.pop()
    if (cb %2==0 and cb%2 == 1):
        sol.append("b")
        es2(n,sol,ca,cb+1)
        sol.pop()

es2(4)