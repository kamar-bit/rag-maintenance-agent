from rag_maintenance_agent.ingest.loader import DocumentLoadError,charger_document,charger_dossier
import rag_maintenance_agent.ingest.loader as loader
from rag_maintenance_agent.ingest.models import Document
import pytest


def test_charger_fichier_txt(tmp_path):
    fichier = tmp_path / "manuel.txt"
    fichier.write_text("Vérifier le moteur.", encoding="utf-8")

    document = charger_document(fichier)

    assert document.contenu == "Vérifier le moteur."
    assert document.source == fichier
    assert document.format == "txt"

def test_charger_fichier_md(tmp_path):
    fichier = tmp_path / "maintenance.md"
    fichier.write_text("# Maintenance\nVérifier le moteur.", encoding="utf-8")

    document = charger_document(fichier)

    assert document.contenu == "# Maintenance\nVérifier le moteur."
    assert document.format == "md"

def test_charger_fichier_pdf(tmp_path, monkeypatch):
    fichier = tmp_path / "manuel.pdf"
    fichier.write_bytes(b"faux contenu PDF")

    class FaussePage:
        def extract_text(self, extraction_mode=None):
            return "Vérifier la pression."

    class FauxLecteurPDF:
        pages = [FaussePage(), FaussePage()]

    monkeypatch.setattr(loader, "PdfReader", lambda chemin: FauxLecteurPDF())

    document = charger_document(fichier)

    assert document.contenu == "Vérifier la pression.\nVérifier la pression."
    assert document.format == "pdf"
    assert document.metadata == {"pages": 2} 

def test_format_non_supporte(tmp_path):
    fichier = tmp_path / "photo.jpg"
    fichier.write_bytes(b"contenu")

    with pytest.raises(DocumentLoadError, match="Format non supporté"):
        charger_document(fichier)

def test_fichier_txt_vide(tmp_path):
    fichier = tmp_path / "vide.txt"
    #apres la creation du chemin on cree le fichier avec write_text qui crée(si file n'existe pas) et ecrit dedans
    fichier.write_text("", encoding="utf-8")

    with pytest.raises(DocumentLoadError, match="fichier est vide"):
        charger_document(fichier)

def test_fichier_inexistant(tmp_path):
    #on crée le chemin vers le fichier mais on ne cree pas le fichie 
    fichier = tmp_path / "absent.txt"

    with pytest.raises(DocumentLoadError, match="Impossible de charger"):
        charger_document(fichier)


def test_charger_dossier_continue_apres_echec(tmp_path, monkeypatch):
    fichier_ok = tmp_path / "bon.txt"
    fichier_erreur = tmp_path / "mauvais.txt"

    fichier_ok.write_text("Moteur vérifié", encoding="utf-8")
    fichier_erreur.write_text("Contenu problématique", encoding="utf-8")

    def faux_charger_document(chemin):
        if chemin == fichier_erreur:
            raise DocumentLoadError("Erreur de lecture")
        return Document(
            contenu="Moteur vérifié",
            source=chemin,
            format="txt",
        )

    monkeypatch.setattr(loader, "charger_document", faux_charger_document)

    rapport = charger_dossier(tmp_path)

    assert len(rapport.documents) == 1
    assert rapport.documents[0].source == fichier_ok
    assert rapport.echecs == {fichier_erreur: "Erreur de lecture"}

