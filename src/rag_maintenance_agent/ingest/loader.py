import logging
from pathlib import Path
logger=logging.getLogger(__name__)
class DocumentLoadError(Exception):
    """Une exception qui gére tous les erreurs lors du chargement d'un document texte"""
def charger_texte(chemin:Path,encoding:str = "utf-8")->str:
    """Charge un fichier texte et retourn son contenu.
    Raises :DocumentLoadError: si le fichier n'existe pas ou si son encodage
    est invalide ou si le fichier est vide 
        """
    try :        
        texte = chemin.read_text(encoding=encoding)
        if not texte.strip():
            logger.error("Fichier vide : %s", chemin)
            raise DocumentLoadError("le fichier est vide") 
        logger.info("le chargement du document a commencé")
        return texte
    except (FileNotFoundError,UnicodeDecodeError) as e:
        logger.error("Échec du chargement : %s", chemin, exc_info=True)
        raise DocumentLoadError(f"Impossible de charger le document : {chemin}") from e
        