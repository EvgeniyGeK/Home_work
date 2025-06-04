import json
from loggers import get_logger


logger = get_logger(name=__file__)

logger.info(f"Начало работы функции read_json_file")
def read_json_file(file_path: str) -> [dict, str]:
    """Функция чтения json файла"""
    try:
        with open(file_path, encoding="utf-8") as f:
            reading_dict = json.load(f)
        logger.info(f"Функция read_json_file успешно завершила свою работу")
        return reading_dict
    except Exception as e:
        # (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError, KeyError):
        logger.exception(f"Обнаружена ошибка: {e}", exc_info=True)
        return []
