'''
Contare le componenti connesse che sono anche alberi
La logica è usare la componente come "visitati"
'''


def componenti(G):
    def DFSr(x,padre,C,c):
        C[x] = c
        for v in G[x]:
            if v == padre:
                continue
            if C[v] != 0:
                return True
            if  DFSr(v,x,C,c):
                return True
        return False
    C = [0] * len(G)
    c = 0
    alberi = 0
    for x in range(len(G)):
        if C[x] == 0:
            c += 1
            ciclo = DFSr(x,-1,C,c)
            if not ciclo:
                alberi += 1

    return C,alberi

G = [[],[2,3],[1,3],[1,2],[5],[4]]
print(componenti(G))

