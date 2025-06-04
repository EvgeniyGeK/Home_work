import logging
import logging.config

from config import PATH


def get_logger(name):
    """Функция для логирования других функций"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(PATH / "log" / "__log_info__.log", mode="a", encoding="UTF-8")
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
