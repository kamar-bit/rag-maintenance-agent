def saluer(nom: str) -> str:
    return f"Bonjour, {nom}, Bienvenue sur le projet ! "


def filtre_urgent(liste: list[str])->list[str] : 
    return [elem for elem in liste if "urgent" in elem.lower() ]
tickets = [
    "Bug urgent",
    "URGENT : serveur arrêté",
    "Problème de connexion"
]
def filtrer_par_mot(tickets : list[str], mot:str="urgent",* ,casse:bool=False)->list[str]:
    """""Filtrer les tickets qui ont le mot recherché.
        Args : casse True majiscule != miniscule 
                casse=True distingue Urgent de urgent
        Returns: les tickets urgent
    """
    if casse==False:
        return [t for t in tickets if mot.lower() in t.lower()]
 
    return [t for t in tickets if mot in t]

print(filtrer_par_mot(tickets))
print(filtrer_par_mot(tickets, casse=True))


