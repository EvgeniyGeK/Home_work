def filter_by_state(user_state: list[dict], state: str) -> list:
    """Функция сортировки словарей по значению ключа"""

    filter_list = []
    for transaction in user_state:
        if "state" not in transaction:
            continue  # пропускаем запись, если нет нужного поля
        elif transaction["state"] == state:
            filter_list.append(transaction)
    return filter_list


def sort_by_date(user_date: list[dict], ascending: bool) -> list[dict]:
    """Функция сортировки по дате"""

    valid_dict = [i for i in user_date if "date" in i]
    return sorted(valid_dict, key=lambda x: x.get("date"), reverse=not ascending)
