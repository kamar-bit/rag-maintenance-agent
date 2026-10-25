from rag_maintenance_agent.hello import saluer,filtre_urgent,filtrer_par_mot

tickets=["c'est urgent wesh","en panne, Urgent !","ça fonctionne mal","hey,urgent","ça ralenti la prod","panne","lent","cassé"]
def test_saluer():
    assert saluer("Maintenance") == "Bonjour, Maintenance, Bienvenue sur le projet ! "
def test_filter():
    assert filtre_urgent(tickets) == ["c'est urgent wesh","en panne, Urgent !","hey,urgent"]
def test_filtrer_par_mot():
    assert filtrer_par_mot(tickets,"Urgent",casse=True) == ["en panne, Urgent !"]
