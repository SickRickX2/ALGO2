def ex3(x):
    T = [1  for i in range(len(x))]
    for i in range(len(x)):
        for j in range(i):
            if x[i] > x[j]:
                T[i] = max(T[i],T[j]+1)

    maxv = max(T)
    seq = []
    for i in range(len(T)-1,-1,-1):
        if T[i] == maxv:
            seq.append(x[i])
            maxv -= 1
    return seq[::-1]

x = (50,4,100,2,48,3,34,30)
#print(ex3(x))

def ex3_b(x):
        T = [i for i in x]
        for i in range(1,len(x)):
            for j in range(i):
                if x[i] > x[j]:
                    T[i] = max(T[i], x[i] + T[j])

        maxv = max(T)
        seq = []

        for i in range(len(x) - 1, -1, -1):
            if T[i] == maxv:
                seq.append(x[i])
                maxv -= x[i]
        return seq[::-1]

#print(ex3_b(x))
def ex3_c(x):
    T = [1]* len(x)
    for i in range(len(x)):
        for j in range(i):
            if x[i] > x[j]:
                T[i] = T[i]+T[j]

    return sum(T)
x = [5,3,7,8,6]
print(ex3_c(x))


