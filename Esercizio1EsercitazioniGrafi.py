'''
Mi creo per prima cosa il vettore delle componenti connesse radicato in zero, dopodiché collego tutte le componenti diverse da quella di zero
a lui in modo tale da rendere il grafo connesso

'''

def connesse(x,G):
    def DFSr(x,G,componenti, c):
        componenti[x] = c
        for y in G[x]:
            if componenti[y] == 0:
                DFSr(y, G, componenti,c)

    componenti = [0] * len(G)
    c = 0
    for x in range(len(G)):
        if componenti[x] == 0:
            c += 1
            DFSr(x, G, componenti,c)
    return componenti

def ex1(G):
    C = connesse(0,G)
    c = 2
    result = []
    for x in range(1,len(G)-1):
        if C[x] == c:
            result.append((0,x))
            c +=1

    return result
G = [
    [1,4],
    [0,4],
    [5,7],
    [6],
    [0,1],
    [2,7],
    [3],
    [2,5]
    ]
print(connesse(0,G))
print(ex1(G))
