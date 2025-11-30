from random import randint

name = "amadou"
print(f"Hello {name}")
print("*" * 50)


# EXERCICES FONCTIONS
# Exercice 1 : Table de multiplication
# Objectif : afficher la table de multiplication d'un nombre donnée


def table_multiplication(nombre, limite):
    """Afficher la table de multiplication d'un nombre jusqu'à une limite"""
    for i in range(1, limite + 1):
        print(f"{nombre} x {i} = {nombre * i}")


# test
table_multiplication(7, 10)


# Exercice 2 : Jeu du "devine le nombre"
def jeu_devine_nombre(nombre_secret, max_tentatives):
    """Deviner un nombre"""
    tentative = 0

    while tentative < max_tentatives:
        try:
            nombre_devine = int(input("Devinez un nombre entre [0-10]: "))
            tentative += 1
            if nombre_devine == nombre_secret:
                print("Gagné")
                break
            elif nombre_devine > nombre_secret:
                print("Trop grand!")
            elif nombre_devine < nombre_secret:
                print("Trop petit !")
        except ValueError as e:
            print("Error :", e)
    else:
        print(f"Perdu ! Le nombre était {nombre_secret}")


jeu_devine_nombre(4, 3)


# Exercice 3 : Configurateur de produit avec **kwargs et combinaison d’arguments
def creer_produit(nom, prix, *categories, remise=0, **attributs):
    """
    Produit avec des informations détaillés

    Args :
        nom : Nom du produit
        prix : Prix du produit
        *categories : Categories du produit (variables)
        remise : Pourcentage de remise appliquée (0 par défaut)
        **attributs : Attributs supplémentaires (couleur, taille, etc.)

    Returns :
        dict : dictionnaire contenant toutes les infos du produit

    """

    prix_discount = prix * (1 - remise / 100)
    attribut_val = ", ".join(f"{cle}:{valeur}" for cle, valeur in attributs.items())
    categories_val = ",".join(categories)

    print(
        f"{"*"*15} {nom} {"*"*15}\n"
        f"PRIX : {prix}\n"
        f"CATEGORIES : {categories_val}\n"
        f"REMISE : {remise}%\n"
        f"PRIX APRES REMISE : {prix_discount:.2f}€\n"
        f"ATTRIBUTS : {attribut_val}\n"
        f"{"*"*(30+2+len(nom))}\n"
    )

    return dict(
        nom=nom,
        prix=prix,
        categories=categories_val,
        remise=remise,
        prix_discount=prix_discount,
        attributs=attribut_val,
    )


## iphone, 990€ , (mobile, neuf), remise=2, couleur=bleu, taille=sm
cc = creer_produit("iphone", 990, "mobile", "neuf", remise=35, couleur="bleu", taille="sm")

print("again cc ",cc)

creer_produit(
    "laptop",
    1200,
    "ordinateur",
    "pro",
    remise=10,
    marque="Dell",
    ram="16GB",
    stockage="512GB SSD",
)

creer_produit(
    "sneakers",
    80,
    "chaussures",
    "sport",
    remise=15,
    couleur="noir",
    taille="42",
    marque="Nike",
)

creer_produit(
    "roman",
    18,
    "livre",
    "fiction",
    remise=5,
    auteur="M. Dupont",
    pages=320,
    langue="français",
)

creer_produit(
    "casque",
    150,
    "audio",
    "neuf",
    remise=20,
    type="sans fil",
    impedance="32ohm",
    poids="250g",
)
