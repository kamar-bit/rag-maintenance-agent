from rag_maintenance_agent.hello import saluer
from rag_maintenance_agent.hello import filtre_urgent

def test_saluer():
    assert saluer("Maintenance") == "Bonjour, Maintenance, Bienvenue sur le projet ! "
def test_filter():
    assert filtre_urgent(["c'est urgent","en panne, urgent !","ça fonctionne mal","urgent","ça ralenti la prod","panne","lent","cassé"]) == ["c'est urgent","en panne, urgent !","urgent"]
