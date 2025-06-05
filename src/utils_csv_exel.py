import csv

import pandas as pd


def read_exel(path_file: str) -> list:
    exel_data = pd.read_excel(path_file).to_dict(orient='records')
    print(exel_data)
    return exel_data