import random

def level1():
    r=random.randint(0,100)
    nombre=int(input("Entrez un nombre entre 0 et 100: "))
    while nombre!=r: 
        if nombre<r:
            print("C'est plus")
        else:
            print("C'est moins")
        nombre=int(input("Entrez un nombre entre 0 et 100: "))

    print("Bravo, vous avez trouvé le nombre mystère !")

def level2():
    r=random.randint(0,1000)
    nombre=int(input("Entrez un nombre entre 0 et 1000: "))
    while nombre!=r:
        if nombre<r:
            print("C'est plus")
        else:
            print("c'est moins")
        nombre=int(input("Entrez un nombre entre 0 et 1000: "))
    print("Bravo, vous avez trouvé le nombre mystère !")

def level3():
    r=random.randint(0,100000)
    nombre=int(input("Entrez un nombre entre 0 et 100000: "))
    while nombre!=r:
        if nombre<r:
            print("C'est plus")
        else: 
            print("C'est moins")
        nombre:int(input("Entrez un nombre entre 0 et 100000: "))
    print("Bravo, vous avez trouvé le nombre mystère !")


level=int(input("Choisissez un niveau de difficulté (1, 2 ou 3): "))
if level==1:
    level1()
elif level==2:
    level2()
elif level==3:
    level3()

while level<1 or level>3:
    level=int(input("Choisissez un niveau de difficulté (1, 2 ou 3): "))
    if level==1:
        level1()
    elif level==2:
        level2()
    elif level==3:
        level3()

    


