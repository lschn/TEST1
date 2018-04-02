import math

def afficheBinairepardivisions() :
    nbr = nb = int(input("Nombre à afficher en binaire : "))
    bits = []
    while True:
        diviseur = nb // 2
        reste = nb % 2
        bits.append(reste)
        if diviseur == 0:
            break
        nb = diviseur
    lon = len(bits)
    #mesure de la longueur
    print(nbr, '= ', end='')
    for i in range(lon) :
        print(bits[lon-1-i], end='')
    #liste inversée pour avoir le bit de poids fort en premier
    print()

def afficheBinaireparquestions() :
    nb = int(input("Nombre à afficher en binaire : "))
    mantisse = math.floor(math.log2(nb))
    print(nb, "= ", end='')
    for i in range (mantisse) :
        puis = 2**(mantisse-i)
        if nb > puis :
            nb -= puis
            print("1", end= '')
        else :
            print("0", end= '')
    print(nb)

def mystere(b,m):
    res = 1
    for j in range(m):
        base = 0
        for k in range (b):
            base = base + 1
        res = res * base
    return res

def mystere2(b,m):
    res = 1
    for j in range(m):
        res = res * b
    return res

def mystere3(b,m):
    return b**m

def reverse():
    chaine = input("entrez une chaine : ")
    mots = chaine.split()
    for i in range(len(mots)):
        print(mots[len(mots) - 1 - i]+" ", end= '')
    print()

for k in range (1,5,2):
    print(k)
    
