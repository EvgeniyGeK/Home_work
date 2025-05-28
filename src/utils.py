import json

def read_json_file(file_path: str) -> [dict, str]:
    """Функция чтения json файла"""
    try:
        with open(file_path, encoding='utf-8') as f:
            reading_dict = json.load(f)
        return reading_dict
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError, KeyError):
        return []