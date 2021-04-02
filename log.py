import logging
import os
import sys

logging.basicConfig(
        format="{\"logger\":\"%(name)s\",\"timestamp\": \"%(asctime)s\" , \"level\": \"%(levelname)s\", \"message\": \"%(message)s\"}",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
        stream=sys.stdout,
        level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)

def log():

    logging.getLogger().setLevel(logging.ERROR)
    if "DEBUG" in os.environ and str(os.environ['DEBUG']).lower() in ['1', 'true', 'yes']:
        logging.getLogger().setLevel(logging.INFO)

    return logging