import random
r=random.randint(0,100)
nombre=int(input("Entrez un nombre entre 0 et 100: "))
while nombre!=r: 
    if nombre<r:
        print("C'est plus")
    else:
        print("C'est moins")
    nombre=int(input("Entrez un nombre entre 0 et 100: "))

print("Bravo, vous avez trouvé le nombre mystère !")

