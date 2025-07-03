def es(n,sol = [],ca = 0,cb = 0):
    if len(sol) == n:
        print("".join(sol))
        return
    if n - len(sol) > (abs(ca-cb)):
        sol.append("c")
        es(n,sol,ca,cb)
        sol.pop()
    if ca-cb>0 or n-len(sol) - abs(ca-cb)>=2:
        sol.append("b")
        es(n,sol,ca,cb+1)
        sol.pop()
    if cb - ca>0  or n-len(sol)- abs(cb-ca)>=2:
        sol.append("a")
        es(n,sol,ca+1,cb)
        sol.pop()
es(3)

