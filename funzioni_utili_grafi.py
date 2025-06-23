'''
VISITA IN PROFONDITÀ DI UN GRAFO (DFS) rappresentato tramite liste di adiacenzq

lo utilizziamo ad esempio per verificare quali nodi siano raggiungibili partendo dal nodo dato in input u

'''


def DFS(u,G):

    def DFSr(u,G,visitati):
        visitati[u] = 1
        for v in G[u]:
            if not visitati[v]:
                DFSr(v,G, visitati)

    n = len(G)
    visitati = [0] * n
    DFSr(u,G, visitati)
    return [x for x in range(n) if visitati[x]]


G = [
    [1],
    [2,3,5],
    [4],
    [5],
    [6],
    [],
    [2]
]
#print(DFS(6,G))
'''
Una visita DFS crea un albero DFS che può essere memorizzato
tramite il vettore dei padri.
Il vettore dei padri P di un albero DFS di un grafo di n nodi ha n componenti:
- Se i è un nodo dell'albero DFS: P[i] contiene il padre del nodo i 
(il padre della radice per convenzione è la radice stessa)
- Se i non fa parte dell'albero P[i] contiene -1
'''

def Padri(u, G):
    def DFSr(u,G,P):
        for v in G[u]:
            if P[v] == -1:
                P[v] = u
                DFSr(v,G,P)
    n = len(G)
    P = [-1] * n
    P[u] = u
    DFSr(u, G, P)
    return P
G = [
    [1],        # Nodo 0: punta a 1
    [],         # Nodo 1: non punta a nulla
    [1, 3, 7],  # Nodo 2: punta a 1, 3, 7
    [7],        # Nodo 3: punta a 7
    [2],        # Nodo 4: punta a 2
    [4],        # Nodo 5: punta a 4
    [4],        # Nodo 6: punta a 4
    [3, 4, 9],  # Nodo 7: punta a 3, 4, 9
    [7],        # Nodo 8: punta a 7
    [0, 2, 8]   # Nodo 9: punta a 0, 2, 8
]

print(Padri(4,G))
