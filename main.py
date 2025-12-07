# .\Scripts\activate
# deactivate
from functools import wraps

print("*" * 60)
print("LES DECORATEUR".center(60))
print("*" * 60)
############################################################################
# DECORATEURS
############################################################################
# 1. décorateurs simple


def mon_decorateur(fonction):
    print(f"Nom de la fonction décorée : {fonction.__name__}")

    def wrapper():
        print("Quelque chose avant l'exécution")
        result = fonction()
        print("Quelque chose après l'exécution")
        return result

    return wrapper


@mon_decorateur
def dire_bonjour():
    print("Bonjour")


dire_bonjour()

print("--" * 20, "Décorateur d'une fonction avec args/kwargs", "--" * 20)

# 2. décorateurs SIMPLE d'une fonction avec des args/kwargs


def decorator_avec_args(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec args : {args}")
        "Appel de additionner avec args : (3,5)"
        return func(*args, **kwargs)

    return wrapper


@decorator_avec_args
def additionner(a, b):
    return a + b


resultat = additionner(3, 5)  # affiche l'information et retourne 8
print(resultat)


print("--" * 20, "Décorateur avec paramètres", "--" * 20)
# 3. décorateurs avec paramètres : c'est une fonction qui retourne un autre décorateur
# c'est une structure a 3 niveaux


def decorateur_avec_params(param1, param2):
    """Fonction externe qui reçoit les paramètres du décorateur"""

    def decorateur_reel(fonction):
        """Le vrai décorateur qui reçoit la fonction"""

        def wrapper(*args, **kwargs):
            """La fonction qui enveloppe la fonction décorée"""
            print(f"Paramètres du décorateur : {param1}, {param2}")
            return fonction(*args, **kwargs)

        return wrapper

    return decorateur_reel


@decorateur_avec_params("Hello", "World")
def ma_fonction():
    print("Fonction exécutée")


ma_fonction()

print("--" * 20, "Application", "--" * 20)


def repeat(nombre_fois):
    """Décorateur qui répète l'éxécution d'une fonction"""

    def mon_decorateur(fonction):
        @wraps(fonction)  # toujours utiliser
        def wrapper(*args, **kwargs):
            print("Nom du Wrapper : ", wrapper.__name__)
            for i in range(nombre_fois):
                print(f"Ma Wokko {i+1} yonn : ", end="")
                fonction(*args, **kwargs)

        return wrapper

    return mon_decorateur


@repeat(4)
def sant_baye():
    """Documentation de ma fonction"""
    print("Dieuredieufé Baye Niass")


sant_baye()
print("Nom de ma fonction : ", sant_baye.__name__)
print("Docs de ma fonction : ", sant_baye.__doc__)

## NB : toujours utiliser les @wraps pour préserver les métadonnées de la fonction oroginale


# EXERCICE 1 : decorateur qui mesure le temps d'exécution
print("--" * 20, "Exercice 1", "--" * 20)

def chronometre():
    """Décorateur qui mesure le temps d'exécution d'une fonction"""
    return ''

def calcul_lent(limit):
    """Calculer la somme des 1_000_000 premiers nombre"""
    resultat = 0
    for i in range(1,limit+1):
        resultat += i;
    print("TEST:::",resultat)


def tri_list(limit):
    """Trier une liste de 10_000 nombres aléatoires"""


calcul_lent(500)

