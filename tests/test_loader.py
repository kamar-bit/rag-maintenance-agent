from rag_maintenance_agent.loader import DocumentLoadError,charger_texte
import pytest

def test_fichier_absent(tmp_path):
    with pytest.raises(DocumentLoadError):
        charger_texte(tmp_path / "inexistant.txt")
def test_fichier_vide(tmp_path):
    fichier = tmp_path / "vide.txt"
    fichier.write_text("", encoding="utf-8")

    with pytest.raises(DocumentLoadError):
        charger_texte(fichier)

def test_encodage_invalide(tmp_path):
    fichier=tmp_path / "xyz.txt"
    fichier.write_bytes(b"\xff")
    with pytest.raises(DocumentLoadError):
        charger_texte(fichier)
def test_fichier(tmp_path):
    fichier = tmp_path / "document.txt"
    fichier.write_text("Bonjour", encoding="utf-8")
    resultat= charger_texte(fichier)
    assert resultat=="Bonjour"