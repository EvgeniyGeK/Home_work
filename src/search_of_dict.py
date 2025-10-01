import re
from collections import Counter


def process_bank_search(transact_data: list[dict], user_request: str) -> list:
    """Функция для поиска в списке словарей операций по строке статус операции"""

    operation_found = [
        transaction
        for transaction in transact_data
        if re.search(user_request, transaction["description"], flags=re.IGNORECASE)
    ]

    return operation_found


def process_bank_operations(data: list[dict], categories: str) -> dict:
    """Функция для подсчета количества банковских операций определенного типа."""

    count_description = {}
    upper_category = categories.upper()
    for x in categories:
        description = [i.get("description") for i in data if i.get("description").upper() in upper_category]
        count_description = Counter(description)

    return count_description

