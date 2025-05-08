def filter_by_currency(transactions: list[dict], currency: str) -> dict:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
           yield i
        # else:
        #    raise "Операций в указанной валюте не найдено"

def transaction_descriptions(transactions: list[dict], description: str) -> str:
    """Функция генератор которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for i in transactions:
        yield i.get("description")


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номер карты"""
    for i in range(start, end + 1):
        count_0 = "0" * (16 - len(str(i)))
        number = count_0 + str(i)
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
