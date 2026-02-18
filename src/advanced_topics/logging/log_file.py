import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug message")
logging.info("Info message")
logging.error("Error occurred")
