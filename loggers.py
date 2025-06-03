import os

import logging
import logging.config

FOLDER_LOG = "log"
def create_log_folder(folder=FOLDER_LOG):
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_logger(name):
    create_log_folder()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f"log/{__name__}.log", mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logging.getLogger()
