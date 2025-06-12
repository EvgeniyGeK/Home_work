import re



def process_bank_search(transactions: dict, user_request: str) -> list[dict[re]]:
    """Функция для поиска в списке словарей операций по строке статус операции"""
    found_dict = []

    for transaction in transactions:
        if re.search(user_request, transaction["state"],flags=re.IGNORECASE):
            found_dict.append(transaction)
        return found_dict










if __name__ == "__main__":
    process_bank_search([
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 593027.0,
        "state": "CANCELED",
        "date": "2023-07-22T05:02:01Z",
        "amount": 30368.0,
        "currency_name": "Shilling",
        "currency_code": "TZS",
        "from": "Visa 1959232722494097",
        "to": "Visa 6804119550473710",
        "description": "Перевод с карты на карту",
    }], "PENDING")
    