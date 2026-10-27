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