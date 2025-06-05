import csv

import pandas as pd


def read_exel(path_file: str) -> list:
    """Функция читает exel файл и преобразует данные в список словарей"""
    try:
        exel_data = pd.read_excel(path_file).to_dict(orient='records')
        return exel_data
    except Exception as e:
        Exception(f'Произошла ошибка: {e}')
        return []
