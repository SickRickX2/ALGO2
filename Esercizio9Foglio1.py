'''
trovare i pozzi raggiungibili partendo da un nodo u in un grafo orientato
'''
def pozzong(u,G):
    def DFS(x,G,visitati):
        visitati[x] = 1
        if not G[x]: return 1
        pozzi = 0
        for y in G[x]:
            if not visitati[y]:
                pozzi += DFS(y,G,visitati)

        return pozzi

    visitati = [0] * len(G)
    return DFS(u,G,visitati)

# Grafo G con 6 nodi (da 0 a 5)
# G[i] è la lista dei nodi raggiungibili da i

G = [
    [1, 2],    # Nodo 0 va a 1 e 2
    [3],       # Nodo 1 va a 3
    [4],       # Nodo 2 va a 4
    [],        # Nodo 3 è un pozzo
    [],        # Nodo 4 è un pozzo
    []         # Nodo 5 è un pozzo, ma non è raggiungibile dagli altri
]

print(pozzong(0,G))