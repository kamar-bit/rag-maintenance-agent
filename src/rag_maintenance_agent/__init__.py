import logging 
from rag_maintenance_agent.config import get_settings

logging.basicConfig(
    level=get_settings().log_level,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
def main() -> None:
    print("Hello from rag-maintenance-agent!")
