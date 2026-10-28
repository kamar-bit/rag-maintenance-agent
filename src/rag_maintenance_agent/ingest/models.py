from dataclasses import dataclass, field
from pathlib import Path
#frozen true : une fois un objet crée ces attributs ne changent plus
@dataclass(frozen=True)
#data class gere le __init__ automatiquement
class Document:
    """Un document chargé, prêt à être découpé en chunks."""
    contenu: str
    source: Path
    format: str
    metadata: dict[str, str | int] = field(default_factory=dict)

@dataclass(frozen=True)
class RapportChargement:
    documents: list[Document]
    echecs: dict[Path, str]

@dataclass(frozen=True)
class Chunk:
    contenu: str
    source: Path
    index:int
    def __post_init__(self):
        if not self.contenu.strip():
            raise ValueError("Le contenu ne peut pas etre vide ")
