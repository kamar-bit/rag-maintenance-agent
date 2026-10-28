from rag_maintenance_agent.ingest.models import Document,Chunk

#on récrit les verif de val au cas ou on fait appel a decouper_chunk sans passer par config
def decouper_document(document:Document,taille:int,chevauchement:int)->list[Chunk]:
    if taille <= 0:
        raise ValueError("La taille doit être supérieure à 0.")

    if chevauchement < 0:
        raise ValueError("Le chevauchement ne peut pas être négatif.")

    if chevauchement >= taille:
        raise ValueError(
            "Le chevauchement doit être inférieur à la taille."
        )
    texte=document.contenu
    chunks :list[Chunk] = []
    debut=0
    index=0
    
    while debut<len(texte):
        fin=min(debut+taille,len(texte))
        contenu_chunk=texte[debut:fin]
        chunk = Chunk(
            contenu=contenu_chunk,
            source=document.source,
            index=index,
            metadata=document.metadata.copy()
        )
        chunks.append(chunk)
        if fin==len(texte):
            break
        index +=1
        debut=fin - chevauchement
    return chunks

