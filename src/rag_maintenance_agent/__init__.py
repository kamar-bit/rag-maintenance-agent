import logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
def main() -> None:
    print("Hello from rag-maintenance-agent!")
