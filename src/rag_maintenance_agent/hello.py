def saluer(nom: str) -> str:
    return f"Bonjour, {nom}, Bienvenue sur le projet ! "


def filtre_urgent(liste: list[str])->list[str] : 
    return [elem for elem in liste if "urgent" in elem.lower() ]


