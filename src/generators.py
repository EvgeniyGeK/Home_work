def filter_by_currency(transactions: list[dict], currency: str) -> dict:
    """
    Итератор, возвращающий транзакции, соответствующие заданной валюте.
    Поддерживаются оба типа структур.
    """
    for t in transactions:
        # Проверяем вложенную структуру (операционный объем)
        if "operationAmount" in t and isinstance(t["operationAmount"], dict):
            op_amount = t["operationAmount"]
            if "currency" in op_amount and isinstance(op_amount["currency"], dict):
                curr = op_amount["currency"].get("code")
                if curr.lower() == currency.lower():
                    yield t

        # Проверяем прямую структуру (currency_code)
        elif "currency_code" in t:
            curr = t.get("currency_code")
            if curr.lower() == currency.lower():
                yield t


def transaction_descriptions(transactions: list[dict], description: str) -> str:
    """Функция генератор которая принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди."""
    for i in transactions:
        yield i.get("description")


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номер карты"""
    for i in range(start, end + 1):
        count_0 = "0" * (16 - len(str(i)))
        number = count_0 + str(i)
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
