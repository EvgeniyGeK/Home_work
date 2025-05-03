def filter_by_currency(transactions: list[dict], currency: str) -> dict:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
           yield i

def transaction_descriptions(transactions: list[dict], description: str) -> str:
    """Функция генератор которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for i in transactions:
        yield i.get("description")


def card_number_generator(start_number: int, stop_number: int):
    number_card = (i for i in range(start_number, stop_number))
    yield number_card