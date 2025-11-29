name = "amadou"
print(f"Hello {name}")
print("*" * 50)


# Exercice 2 : Évaluateur de mot de passe
# Objectif : créer un programme qui évalue la force d'un mot de passe


def evaluer_mot_de_passe(mot_de_passe):
    len_mp = len(mot_de_passe)
    match len_mp:
        case n if n < 6:
            return "Très faible"
        case n if n <= 7:
            return "Faible"
        case n if n <= 11:
            return "Moyen"
        case _:
            return "Fort"


def est_securise(mot_de_passe):
    return "Sécurisé" if len(mot_de_passe) >= 8 else "Non sécurisé"


print(f"Sécurité du mot de passe 'test' = {evaluer_mot_de_passe("test")}")
print(f"Sécurité du mot de passe '1azerty' = {evaluer_mot_de_passe("1azerty")}")
print(f"Sécurité du mot de passe '1234azerty!' = {evaluer_mot_de_passe("1234azerty!")}")
print(
    f"Sécurité du mot de passe '123azertyoihidniohi' = {evaluer_mot_de_passe("123azertyoihidniohi")}"
)

print(f"'azerty' => {est_securise("azerty")}")
print(f"'1234azerty' => {est_securise("1234azerty")}")
