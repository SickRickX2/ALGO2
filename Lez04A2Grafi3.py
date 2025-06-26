def calcola_percorso(P, n, nodi_percorsi):
    while n != P[n]:
        nodi_percorsi[n] += 1
        n = P[n]
    nodi_percorsi[n] += 1

def calcola_distanza(P, u, v):
    nodi_percorsi = [0] * len(P)
    calcola_percorso(P, u, nodi_percorsi)
    calcola_percorso(P, v, nodi_percorsi)
    distanza = 0
    for i in range(len(nodi_percorsi)):
        if nodi_percorsi[i] == 1:
            distanza += 1
    return distanza

P = [1, 1, 0, 1, 0, 2, 2, 4]
print(calcola_distanza(P, 7, 6))