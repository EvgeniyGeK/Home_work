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


def read_csv(path_to_file: str) -> list:
    csv_dict = []
    try:
        with open(path_to_file, encoding='utf-8') as file:
            csv_data = csv.DictReader(file, delimiter=';')
            for row in csv_data:
                csv_dict.append(row)
                return csv_dict
    except Exception as e:
        Exception(f'Произошла ошибка: {e}')
        return []
