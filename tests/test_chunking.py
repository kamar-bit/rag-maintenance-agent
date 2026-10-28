from pathlib import Path
import pytest

from rag_maintenance_agent.ingest.chunking import decouper_document
from rag_maintenance_agent.ingest.models import Document


def creer_document(texte: str) -> Document:
    return Document(
        contenu=texte,
        source=Path("manuel.pdf"),
        format="pdf",
        metadata={},
    )


def test_document_vide():
    document = creer_document("")

    chunks = decouper_document(
        document,
        taille=800,
        chevauchement=100,
    )

    assert chunks == []


def test_texte_plus_court_que_taille_chunk():
    document = creer_document("Vérifier le niveau d'huile.")

    chunks = decouper_document(
        document,
        taille=800,
        chevauchement=100,
    )

    assert len(chunks) == 1
    assert chunks[0].contenu == document.contenu
    assert chunks[0].index == 0
    assert chunks[0].source == document.source


def test_chevauchement_negatif():
    document = creer_document("Un texte de test.")

    with pytest.raises(ValueError):
        decouper_document(
            document,
            taille=10,
            chevauchement=-1,
        )


def test_plusieurs_chunks_avec_chevauchement():
    document = creer_document("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    chunks = decouper_document(
        document,
        taille=10,
        chevauchement=2,
    )

    assert len(chunks) == 3
    assert [chunk.index for chunk in chunks] == [0, 1, 2]
    assert chunks[0].contenu == "ABCDEFGHIJ" 
    assert chunks[1].contenu == "IJKLMNOPQR" 
    assert chunks[2].contenu == "QRSTUVWXYZ" 
    assert chunks[0].contenu[-2:] == chunks[1].contenu[:2]
    assert chunks[1].contenu[-2:] == chunks[2].contenu[:2]

def test_chevauchement_egale_taille():
    document = creer_document("Un texte de test.")

    with pytest.raises(ValueError):
        decouper_document(
            document,
            taille=10,
            chevauchement=10,
        )

def test_taille_nulle():
    document = creer_document("Un texte de test.")

    with pytest.raises(ValueError):
        decouper_document(
            document,
            taille=0,
            chevauchement=0,
        )

