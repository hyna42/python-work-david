# .\Scripts\activate
# deactivate

print("*" * 60)
print("LES DECORATEUR".center(60))
print("*" * 60)
############################################################################
# DECORATEURS
############################################################################

def mon_decorateur(fonction):
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