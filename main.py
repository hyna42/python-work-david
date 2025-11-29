name = "amadou"
print(f"Hello {name}")
print("*" * 50)


# Exercice 3 : Distributeur de boissons avec match-case
def distributeur_boisson(choix, monnaie):
    match choix:
        case "cafe":
            prix= 1.5
            nom="café"

        case "the":
            prix= 1.2
            nom="thé"

        case "chocolat":
            prix= 2
            nom="chocolat"

        case "eau":
            prix= 0.8
            nom="eau"

        case _:
            return "Boisson non disponible"
        
    #vérification de la monnie
    if monnaie >= prix:
        return f"Voici votre {nom} - Monnaie : {monnaie-prix:.2f}€"
    else:
        return f"Insuffisant ! Il manque {prix-monnaie:.2f}€"

#TESTS
choix="javel"
monnaie=4
print(distributeur_boisson(choix,monnaie))