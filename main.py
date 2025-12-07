# .\Scripts\activate
# deactivate

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

print("--" * 20,"Décorateur d'une fonction avec args/kwargs","--" * 20)

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


print("--" * 20,"Décorateur avec paramètres","--" * 20)
# 3. décorateurs avec paramètres : c'est une fonction qui retourne un autre décorateur

def decorateur_avec_params(param1, param2):
    """Fonction externe qui reçoit les paramètres du décorateur"""
    def decorateur_reel(fonction):
        """Le vrai décorateur qui reçoit la fonction"""
        def wrapper(*args,**kwargs):
            """La fonction qui enveloppe la fonction décorée"""
            print(f"Paramètres du décorateur : {param1}, {param2}")
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur_reel



@decorateur_avec_params("Hello","World")
def ma_fonction():
    print("Fonction exécutée")
ma_fonction()
