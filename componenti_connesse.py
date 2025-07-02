'''
avendo un grafo non orientato trovare le componenti connesse
'''

G = [[1],
     [0,2],
     [1],
     [4],
     [3]    ]

def connesse(G):
    def DFS(x, G, visitati):
        visitati[x] = 1
        for v in G[x]:
            if not visitati[v]:
                DFS(v,G,visitati)

    visitati = [0] * len(G)
    componenti = 0
    for x in range(len(G)):
        if not visitati[x]:
            DFS(x,G,visitati)
            componenti +=1
    return componenti



print(connesse(G))
