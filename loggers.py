import os

import logging
import logging.config

from config import PATH

FOLDER_LOG = "log"
def create_log_folder(folder=FOLDER_LOG):
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_logger():
    # create_log_folder()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler( PATH / "log" / "__name__.log", mode='a', encoding='UTF-8')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
