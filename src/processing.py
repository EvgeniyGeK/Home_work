def filter_by_state(user_state: list[dict], state: str = "EXECUTED") -> [list, str]:
    """Функция сортировки словарей по значению ключа"""
    filter_list = []
    for key in user_state:
        if key not in user_state:
            return "Ключ не найден"
        elif key.get("state") == state:
            filter_list.append(key)
    return filter_list


def sort_by_date(user_date: list[dict], ascending: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    for key in user_date:
        if key not in user_date:
            raise ValueError("Дата отсутствует")
        else:
            return sorted(user_date, key=lambda x: x.get("date"), reverse=ascending)

    # elif "date" not in user_date:
    #     return sorted(user_date, key=lambda x: x["id"])



