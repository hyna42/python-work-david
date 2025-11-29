name = "amadou"
print(f"Hello {name}")
print("*" * 50)

# FONCTIONS


# (1) argument multiples *args / **kwargs
# *args -->définit un tuple (n,)
def som(*args):
    total = 0
    for i in args:
        total += i
    return total


nombre = (10, 2, 3, 8)
print(f"Somme de ({nombre}) = {som(*nombre)}")


# **kwargs -> prstock les args dans un dictionnaire clé=valeur
def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")


afficher_infos(nom="Justine", age=25, profession="Développeuse")

print("*" * 10 + "fonctions" + "*" * 10)
# (2) fonction = objet de première classe
# #en python les fonctions sont des objets de première classe : elle peuvent être assignées à des variables, passées comme argument et retournées par d'autre fonctions


def dire_bonjour():
    return "Bonjour!"


def dire_aurevoir():
    return "Au revoir!"


def choisir_salutation(moment):
    if moment == "matin":
        return dire_bonjour  # retourn la référence à la fonction sans les ()
    else:
        return dire_aurevoir


# utilisation
salutation = choisir_salutation("soir")
print(salutation())


# (3) fonction d'ordre supérieur
def appliquer_operation(liste, operation):
    return [operation(x) for x in liste]


def double(x):
    return x * 2


def carre(x):
    return x**2

#utilisation
liste = [1,2,3,4,5]
resultat = appliquer_operation(liste,carre)
print(f"Résultat : {resultat}")

# (4) fonction lamda = anonyme , lambda argument : expression
nombres = [1,2,3,4,5]
print(f"double = {appliquer_operation(nombres,lambda x : x * 2)}")
print(f"carre = {appliquer_operation(nombres,lambda x : x ** 2)}")
