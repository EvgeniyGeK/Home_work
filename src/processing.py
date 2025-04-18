def filter_by_state(user_data: list[dict], state: str = 'EXECUTED') -> list:
    """Функция сортировки словарей по значению ключа"""
    filter_list = []
    for key in user_data:
        if key.get('state') == state:
            filter_list.append(key)
    return filter_list

