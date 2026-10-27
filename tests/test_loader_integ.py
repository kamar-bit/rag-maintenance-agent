from rag_maintenance_agent.ingest.loader import DocumentLoadError,charger_document
from pathlib import Path

CORPUS = Path("corpus")
def test_charger_vrai_corpus():
    assert CORPUS.is_dir(), "Le dossier corpus/ n'existe pas"
    fichiers = [
        chemin
        for chemin in CORPUS.iterdir()
        if chemin.is_file()
        and chemin.suffix.lower() in {".txt", ".md", ".pdf"}
    ]
    #verifier qu'on a trouvé des fichiers dans list fichier n'est pas vide
    #le message est affiché uniquement si la condition est fausse
    assert fichiers, "Aucun document trouvé dans corpus/"

    for fichier in fichiers:
        document = charger_document(fichier)
        #verifier que le fichier n'est pas vide 
        assert document.contenu.strip(), f"Document vide : {fichier}"
        assert document.format == fichier.suffix.lower().lstrip(".")

        print(
            f"\nNom : {fichier.name}"
            f"\nFormat : {document.format}"
            f"\nLongueur : {len(document.contenu)} caractères"
            f"\nExtrait : {document.contenu[:200]}"
        )