def es4(n,sol = []):
    if len(sol) == n:
        print("".join(sol))
        return

    for k in ['1','2','3','4']:
        if len(sol) == 0:
            sol.append(k)
            es4(n,sol)
            sol.pop()

        elif (abs(int(k)-int(sol[-1]))) >= 2:
            sol.append(k)
            es4(n,sol)
            sol.pop()

es4(3)





