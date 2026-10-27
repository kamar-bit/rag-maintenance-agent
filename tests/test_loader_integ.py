from pathlib import Path

from rag_maintenance_agent.ingest.loader import charger_dossier

CORPUS = Path("corpus")


def test_charger_vrai_corpus():
    assert CORPUS.is_dir(), "Le dossier corpus/ n'existe pas"

    rapport = charger_dossier(CORPUS)

    assert rapport.documents, "Aucun document n'a été chargé"

    for document in rapport.documents:
        assert document.contenu.strip(), (
            f"Document vide : {document.source}"
        )
        assert document.format == (
            document.source.suffix.lower().lstrip(".")
        )

        print(
            f"\nNom : {document.source.name}"
            f"\nFormat : {document.format}"
            f"\nLongueur : {len(document.contenu)} caractères"
            f"\nExtrait : {document.contenu[:200]}"
        )

    print(f"\nDocuments chargés : {len(rapport.documents)}")
    print(f"Échecs : {len(rapport.echecs)}")

    for chemin, raison in rapport.echecs.items():
        print(f"Échec : {chemin} — {raison}")
