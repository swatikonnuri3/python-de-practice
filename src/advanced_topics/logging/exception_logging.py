import logging
try:
    x = 10 / 0
except Exception as e:
    logging.exception("Exception occurred")
