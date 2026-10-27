import logging
from pathlib import Path
from pypdf import PdfReader
from pypdf.errors import PdfReadError
from rag_maintenance_agent.ingest.models import Document ,RapportChargement


class DocumentLoadError(Exception):
    """Une exception qui gére tous les erreurs lors du chargement d'un document texte"""

logger=logging.getLogger(__name__)


def _lire_texte(chemin: Path) -> Document:
    contenu = None
    encodages = ("utf-8", "utf-8-sig", "cp1252")

    for encodage in encodages:
        try:
            contenu = chemin.read_text(encoding=encodage)
            if encodage != "utf-8":
                logger.warning(
                    "Encodage de remplacement utilisé pour %s : %s",
                    chemin,
                    encodage,
                )
            break
        except UnicodeDecodeError:
            continue

    if contenu is None:
        raise DocumentLoadError(
            f"Impossible de décoder le fichier avec les encodages pris en charge : {chemin}"
        )

    if not contenu.strip():
        raise DocumentLoadError(f"Le fichier est vide : {chemin}")

    return Document(
        contenu=contenu,
        source=chemin,
        format=chemin.suffix.lower().lstrip("."),
    )


def _lire_pdf(chemin: Path) -> Document:
    try:
        lecteur = PdfReader(chemin)

        if lecteur.is_encrypted:
            raise DocumentLoadError(
                f"PDF protégé par mot de passe : {chemin}"
            )

        pages = [
            page.extract_text(extraction_mode="layout") or ""
            for page in lecteur.pages
        ]

        contenu = "\n".join(pages).strip()

    except PdfReadError as e:
        logger.warning("Impossible de lire le PDF %s : %s", chemin, e)
        raise DocumentLoadError(
            f"PDF corrompu ou illisible : {chemin}"
        ) from e

    if not contenu:
        logger.warning(
            "Aucun texte extractible dans le PDF : %s",
            chemin,
        )
        raise DocumentLoadError(
            f"PDF vide ou scanné : aucun texte extractible dans {chemin}"
        )

    return Document(
        contenu=contenu,
        source=chemin,
        format="pdf",
        metadata={"pages": len(lecteur.pages)},
    )


#pour choisir le lecteur approprié pour chaque doc
LECTEURS = {
    ".txt": _lire_texte,
    ".md": _lire_texte,
    ".pdf": _lire_pdf,
}



def charger_document(chemin: Path) -> Document:
    lecteur = LECTEURS.get(chemin.suffix.lower())

    if lecteur is None:
        logger.error("Format non supporté : %s", chemin.suffix)
        raise DocumentLoadError(
            f"Format non supporté : {chemin.suffix}"
        )

    try:
        document = lecteur(chemin)
    except (FileNotFoundError, PdfReadError) as e:
        logger.error("Échec du chargement : %s", chemin, exc_info=True)
        raise DocumentLoadError(
            f"Impossible de charger le document : {chemin}"
        ) from e
    

    logger.info("Document chargé : %s", chemin)
    return document

def charger_dossier(dossier: Path) -> RapportChargement:
    documents = []
    echecs = {}

    for chemin in dossier.rglob("*"):
        if not chemin.is_file():
            continue

        if chemin.suffix.lower() not in {".txt", ".md", ".pdf"}:
            logger.warning(f"Format non pris en charge, fichier ignoré:{chemin}")
            continue

        try:
            document = charger_document(chemin)
            documents.append(document)
        except DocumentLoadError as e:
            echecs[chemin] = str(e)

    return RapportChargement(
        documents=documents,
        echecs=echecs,
    )