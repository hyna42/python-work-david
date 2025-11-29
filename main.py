from random import randint;

name = "amadou"
print(f"Hello {name}")
print("*" * 50)


# EXERCICES FONCTIONS
# Exercice 1 : Table de multiplication
#Objectif : afficher la table de multiplication d'un nombre donnée

def table_multiplication(nombre, limite):
    """Afficher la table de multiplication d'un nombre jusqu'à une limite"""
    for i in range(1,limite + 1):
        print(f"{nombre} x {i} = {nombre * i}")

#test
table_multiplication(7,10)


#Exercice 2 : Jeu du "devine le nombre"
def jeu_devine_nombre(nombre_secret, max_tentatives):
    """Deviner un nombre"""
    tentative = 0
  

    while( tentative < max_tentatives):
        try:
            nombre_devine=int(input("Devinez un nombre entre [0-10]: "))
            tentative += 1
            if nombre_devine == nombre_secret:
                print("Gagné")
                break
            elif nombre_devine > nombre_secret:
                print("Trop grand!")
            elif nombre_devine < nombre_secret:
                print("Trop petit !")
        except ValueError as e:
            print("Error :",e)
    else:
        print(f"Perdu ! Le nombre était {nombre_secret}")

jeu_devine_nombre(4,3)


#Exercice 3 : Configurateur de produit avec **kwargs et combinaison d’arguments
