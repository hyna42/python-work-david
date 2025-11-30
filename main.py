from random import randint

name = "amadou"
print(f"Hello {name}")
print("*" * 50)


# EXERCICES FONCTIONS
# Exercice 1 : Table de multiplication
# Objectif : afficher la table de multiplication d'un nombre donnée

print("**** Exercice 1 ****".center(60))
def table_multiplication(nombre, limite):
    """Afficher la table de multiplication d'un nombre jusqu'à une limite"""
    for i in range(1, limite + 1):
        print(f"{nombre} x {i} = {nombre * i}")


# test
table_multiplication(7, 10)

print("**** Exercice 2 ****".center(60))
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

print("**** Exercice 3 ****".center(60))
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

    #validation de la remise
    if not 0 <= remise <= 100:
        print(f"Remise invalide ({remise}%), mise à 0")
        remise=0
    #calcul du prix après remise
    prix_discount = prix * (1 - remise / 100)

    #affichage formaté :  produit et remise
    print(f"\n  Poduit : {nom}")
    print(f"   Prix Original : {prix:.2f}")

    if remise > 0:
        print(f"   Remise : {remise}%")
        print(f"   Prix final : {prix_discount:.2f}€ (économie de {prix-prix_discount:.2f}€)")
    else:
        print(f"   Prix final : {prix_discount:.2f}€")

    #affichage des catégories
    if categories:
        print(f"   Catégories : {','.join(categories)}")
    else:
        print(f"   Categories : Aucune")

    #affichage des attributes supplémentaires
    if attributs:
        print(f"   Attributs : {','.join(f"{cle}:{valeur}" for cle, valeur in attributs.items())}")

    #creation du disctionnaire

    return dict(
        nom=nom,
        prix_original=prix,
        remise=remise,
        prix_final=prix_discount,
        categories=list(categories),
        attributs=attributs,
    )
#TEST : creer_produit()
creer_produit(
    "iphone",                    # nom
    990,                         # prix
    "mobile", "neuf",            # *categories
    remise=2,                    # remise
    couleur="bleu",              # **attributs
    taille="sm"                  # **attributs
)


def afficher_catalogue(*produits):
    """
    Args :
        *produits: plusieurs produits (dict)
    Returns:
        catalogue formaté
    """
    print("=" * 60)
    print("CATALOGUE DE PRODUITS".center(60))
    print("=" * 60)
    #validation du catalogue
    if not produits:
        print("Aucun produit dans le catalogue")
        return
    print(f"\nNombre de produits : {len(produits)}")
    
    for i, produit in enumerate(produits,1):
        print(f"{i}. {produit['nom']} - {produit['prix_final']:.2f}€",end="")
        if produit['remise'] > 0:
            print(f" (remise de {produit['remise']}%)",end="")
        if produit['categories']:
            print(f"  Categories : {','.join(produit['categories'])}")
    
    # Calcul du prix total
    prix_total = sum(p['prix_final'] for p in produits)
    print(f"\nPrix total du catalogue {prix_total:.2f}")
    
    print("=" * 60)
    print("FIN CATALOGUE DE PRODUITS".center(60))
    print("=" * 60)


#TEST afficher_catalogue()

p1 = creer_produit(
    "laptop",
    1200,
    "ordinateur",
    "pro",
    remise=10,
    marque="Dell",
    ram="16GB",
    stockage="512GB SSD",
)

p2=creer_produit(
    "sneakers",
    80,
    "chaussures",
    "sport",
    remise=15,
    couleur="noir",
    taille="42",
    marque="Nike",
)

p3=creer_produit(
    "roman",
    18,
    "livre",
    "fiction",
    remise=5,
    auteur="M. Dupont",
    pages=320,
    langue="français",
)

p4=creer_produit(
    "casque",
    150,
    "audio",
    "neuf",
    remise=20,
    type="sans fil",
    impedance="32ohm",
    poids="250g",
)

afficher_catalogue(p1,p2,p3,p4)