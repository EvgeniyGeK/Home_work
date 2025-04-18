def filter_by_state(user_state: list[dict], state: str = "EXECUTED") -> list:
    """Функция сортировки словарей по значению ключа"""
    filter_list = []
    for key in user_state:
        if key.get("state") == state:
            filter_list.append(key)
    return filter_list


def sort_by_date()