def es5(n,sol = []):
    if len(sol) == n:
        print("".join(sol))
        return
    for k in range(1,n+1):
        if len(sol)== 0:
            sol.append(str(k))
            es5(n,sol)
            sol.pop()
        elif str(k) not in sol and (int(sol[-1]))%2 == 0 and k%2 == 1:
            sol.append(str(k))
            es5(n,sol)
            sol.pop()
        elif str(k) not in sol and (int(sol[-1]))%2 == 1 and k%2 == 0:
            sol.append(str(k))
            es5(n,sol)
            sol.pop()
es5(4)