
name = "amadou"
print(f"Hello {name}")
print("*"*50)

#Exercice 1 : Calculateur de tarif de cinéma
#Objectif : Créez un programme qui calcule le prix d’une place de cinéma en fonction de l’âge du spectateur.


def calculer_tarif(age):
    """calcule le tarif d'une place de cinéma selon l'âge"""
    if age <= 5:
        return 0
    elif age <= 17:
        return 7
    elif age <= 64:
        return 12
    else:
        return 8

print(f"3 ans : {calculer_tarif(3)}€")
print(f"12 ans : {calculer_tarif(12)}€")
print(f"63 ans : {calculer_tarif(63)}€")
print(f"70 ans : {calculer_tarif(70)}€")




print("*"*10+" match-case "+"*"*10)
def calculer_tarif_bis(age):
    """calcule le tarif d'une place de cinéma selon l'âge via match-case"""
    match age:
        case age if age<= 5:
            return 0
        case age if age<= 17:
            return 7
        case age if age<= 64:
            return 12
        case _:
            return 8

        
print(f"3 ans : {calculer_tarif_bis(3)}€")
print(f"12 ans : {calculer_tarif_bis(12)}€")
print(f"63 ans : {calculer_tarif_bis(63)}€")
print(f"70 ans : {calculer_tarif_bis(70)}€")
    