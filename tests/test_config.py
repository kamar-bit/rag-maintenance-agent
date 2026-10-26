from rag_maintenance_agent.config import get_settings
def test_settings_lit_l_environnement(monkeypatch):
    monkeypatch.setenv("RAG_LLM_API_KEY", "cle-de-test")
    monkeypatch.setenv("RAG_CHUNK_SIZE", "500")
    get_settings.cache_clear()
    s = get_settings()
    assert s.chunk_size == 500
    assert s.llm_api_key.get_secret_value() == "cle-de-test"