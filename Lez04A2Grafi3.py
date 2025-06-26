def calcola_percorso(P,x,y):
    n = 0
    while n < len(P):
        n +=1
        if P[x] == y:
            return True,n
        if P[x] == P[y]:
            return True,n+1
        x = P[x]
    return False, n

def calcola_distanza(P,u,v):
     UV_check,UV_dist= calcola_percorso(P,u,v)
     VU_check,VU_dist= calcola_percorso(P,v,u)
     if not UV_check and not VU_check:
        return "nessun percorso trovato"
     if UV_check: return UV_dist
     return VU_dist

P = [1, 1, 0, 1, 0, 2, 2, 4]
print(calcola_distanza(P,3,4))