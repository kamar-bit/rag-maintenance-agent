# ingest/__init__.py
from .loader import DocumentLoadError, charger_texte
#les imports deviennent courts charger_texte accessible via ingest
#si qlq import tous * depuis ingest on lui donne que ces fct DocumentLoad et charger
#init expose les deux fct
__all__ = ["DocumentLoadError", "charger_texte"]