from rag_maintenance_agent.hello import saluer
def test_saluer():
    assert saluer("Maintenance") == "Bonjour, Maintenance, Bienvenue sur le projet ! "