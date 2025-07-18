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


'''G = [
    [1],
    [2,3,5],
    [4],
    [5],
    [6],
    [],
    [2]
]'''
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

#print(Padri(4,G))


'''
restituisce il cammino dal nodo radice dell'albero P al nodo u
'''
def CamminoR(u, P):
    if P[u] == -1: return []
    if P[u] == u: return [u]
    return CamminoR(P[u], P) + [u]

'''
L'algoritmo produce una bi-colorazione se il grafo G è bicolorabile altrimenti restituisce una lista vuota
'''
def Colora(G):

    def DFSr(x,G,Colore,c):
        Colore[x] = c
        for y in G[x]:
            if Colore[y] == -1:
                if not DFSr(y,G,Colore,1-c):
                    return False
            elif Colore[y] == Colore[x]:
                return False
        return True

    Colore = [-1] * len(G)
    if DFSr(0,G,Colore,0):
        return Colore
    return []


def Componenti(G):
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

'''G = [
    [2,6],
    [7,8],
    [0,6,16,10],
    [11,18],
    [],
    [12,14,17],
    [2,0],
    [1,15],
    [1,13],
    [15,13],
    [2,16],
    [3,18],
    [5,14,17],
    [8,9],
    [12,17,5],
    [7,9],
    [10,2],
    [5,14,12],
    [3,11]

]
#print(Componenti(G))
'''
def Trasposto(G):
    GT = [[]for _ in range(len(G))]
    for x in range(len(G)):
        for y in G[x]:
            GT[y].append(x)

    return GT



def FConnessa(x,G):
    visitati1 = DFS(x,G)
    G1 = Trasposto(G)
    visitati2 = DFS(x,G1)
    componente = []
    for i in range(len(G)):
        if visitati1[i] == visitati2[i] == 1:
            componente.append(i)
    return componente


def compFC(G):
    FC = [0] * len(G)
    c = 0
    for i in range(len(G)):
        if FC[i] == 0:
            E = FConnessa(i,G)
            c += 1
            for x in E:
                FC[x] = c
    return FC

def sortTop(G):
    n = len(G)
    gradoEnt = [0] * n
    for i in range(n):
        for j in G[i]:
            gradoEnt[j] += 1
    sorgenti = [i for i in range(len(G)) if gradoEnt[i] == 0]
    ### codice per trovare le sorgenti

    ST = []
    while sorgenti:
        u = sorgenti.pop()
        ST.append(u)
        for v in G[u]:
            gradoEnt[v] -= 1
            if gradoEnt[v] == 0:
                sorgenti.append(v)
    if len(ST) == len(G): return ST
    return []

def sortTop1(G):

    def DFSr(u, G, visitati, lista):
        visitati[u] = 1
        for v in G[u]:
            if visitati[v] == 0:
                DFSr(v,G,visitati,lista)
        lista.append(u)


    visitati = [0] * len(G)
    lista = []
    for u in range(len(G)):
        if visitati[u] == 0:
            DFSr(u, G, visitati, lista)
    lista.reverse()
    return lista

#G = [[1,6,5],[2,6],[],[2,4,6],[5,6],[],[2,5]]


#print(sortTop(G))
#print(sortTop1(G))


'''
trovare cicli in:
1) grafi non diretti
2) grafi diretti
'''

def ciclo(u, G):
    visitati = [0] * len(G)
    return DFSr (u,u, G, visitati)
def DFSr(u,padre,G,visitati):
    visitati[u] = 1
    for v in G[u]:
        if visitati[v] == 1:
            if v != padre: return True

        else:
            if DFSr(v,u,G,visitati):
                return True
    return False

def DFSr(u,G,visitati):
    visitati[u] =1
    for v in G[u]:
        if visitati[v] == 1:
                return True
        if visitati[v] == 0:
            if DFSr(v,G,visitati):
                return True
    visitati[u] = 2
    return False

def cicloD(u,G):
    visitati = [0] * len(G)
    return DFSr(u,G,visitati)

def cicloD1(G):
    visitati = [0] * len(G)
    for u in range(len(G)):
        if visitati[u] == 0:
            if DFSr(u,G,visitati):
                return True
    return False


def trova_ponti(G):
    def dfs(x,padre,altezza,ponti):
        # assegna l'altezza del nodo corrente
        if padre == -1:
            altezza[x] = 0
        else:
            altezza[x] = altezza[padre] +1
        #minima altezza raggiungibile dal sottoalbero
        min_raggiungibile = altezza[x]
        for y in G[x]:
            if altezza[y] == -1:
                #il nodo y non è stato ancora visitato
                b = dfs(y,x,altezza,ponti)
            if b > altezza[x]:
                #altezza di x è minore di quella ritornata da y
                #quindi (x,y) è un ponte
                ponti.append(x,y)
                min_raggiungibile = min(min_raggiungibile,b)
            elif y != padre:
                #y già visitato e (x,y) è un arco all'indietro
                min_raggiungibile = min(min_raggiungibile,altezza[y])
            return min_raggiungibile
    altezza = [-1] * len(G)
    ponti = []
    # inizia la DFS dal nodo 0
    dfs(0, -1, altezza, ponti)
    return ponti


'''
visita in ampiezza di BFS
'''

def BFS(x,G):
    visitati = [0] * len(G)
    visitati[x] = 1
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i +=1
        for y in G[u]:
            if visitati[y] == 0:
                visitati[y] = 1
                coda.append(y)

    return visitati
'''
padri BFS
'''

def BFSpadri(x,G):
    P = [-1] * len(G)
    P[x] = x
    coda = [x]
    i = 0
    while len(coda)>i:
        u =coda[i]
        i += 1
        for y in G[u]:
            if P[y] == -1:
                P[y] = u
                coda.append(y)
    return P

#G= [[1,5],[2],[3],[4],[],[2,4],[2]]
#print(BFSpadri(2,G))


def BFSdistanze(x,G):
    D = [-1] * len(G)
    D[x] = 0
    coda = [x]
    i = 0
    while len(coda) >i:
        u = coda[i]
        i +=1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u] + 1
                coda.append(y)
    return D

G= [[1,5],[2],[3],[4],[],[2,4],[2]]
print(BFSdistanze(G))
