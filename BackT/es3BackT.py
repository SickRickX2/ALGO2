def es3(n,sol=[]):
    if len(sol) == n:
        print("".join(sol)+"".join(sol[::-1]))
        return
    else:
        sol.append("a")
        es3(n,sol)
        sol.pop()
        sol.append("b")
        es3(n,sol)
        sol.pop()
es3(2)