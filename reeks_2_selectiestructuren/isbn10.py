cijfers = []
for i in range(10):
    cijfers.append(int(input()))

def berekenISBN(cijfers):
    tussen_som = 0
    for i in range(len(cijfers) - 1):
        tussen_som += (i+1) * cijfers[i]
    resul = tussen_som % 11
    return resul

def controleer(cijfers):
    return 'OK' if cijfers[-1] == berekenISBN(cijfers) else 'FOUT'

print(controleer(cijfers))