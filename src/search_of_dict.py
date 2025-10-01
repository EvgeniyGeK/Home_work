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



if __name__ == "__main__":
    process_bank_operations(
        [
            {
                "id": 286706711,
                "state": "EXECUTED",
                "date": "2018-02-06T06:42:02.219233",
                "operationAmount": {"amount": "621.37", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "MasterCard 9175985085449563",
                "to": "Счет 82781399328834147668",
            },
            {
                "id": 921286598,
                "state": "EXECUTED",
                "date": "2018-03-09T23:57:37.537412",
                "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 26406253703545413262",
                "to": "Счет 20735820461482021315",
            },
            {
                "id": 649467725,
                "state": "EXECUTED",
                "date": "2018-04-14T19:35:28.978265",
                "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 27248529432547658655",
                "to": "Счет 97584898735659638967",
            },
            {
                "id": 902831954,
                "state": "EXECUTED",
                "date": "2018-04-22T17:01:46.885252",
                "operationAmount": {"amount": "84732.61", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 3530191547567121",
                "to": "Счет 46878338893256147528",
            },
            {
                "id": 280743947,
                "state": "EXECUTED",
                "date": "2018-09-27T14:26:24.629306",
                "operationAmount": {"amount": "45653.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 23177857685058835559",
                "to": "Счет 56363465303962313778",
            },
            {
                "id": 547682597,
                "state": "EXECUTED",
                "date": "2018-12-29T21:45:18.495053",
                "operationAmount": {"amount": "66263.93", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 77977573135347241529",
                "to": "Счет 33062909508148771891",
            },
            {
                "id": 871921546,
                "state": "EXECUTED",
                "date": "2019-02-14T03:09:23.006652",
                "operationAmount": {"amount": "47022.09", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Classic 6216537926639975",
                "to": "Счет 67667879435628279708",
            },
            {
                "id": 633268359,
                "state": "EXECUTED",
                "date": "2019-07-12T08:11:47.735774",
                "operationAmount": {"amount": "2631.44", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Gold 3589276410671603",
                "to": "Счет 96292138399386853355",
            },
            {
                "id": 122284694,
                "state": "EXECUTED",
                "date": "2019-08-08T21:58:06.688541",
                "operationAmount": {"amount": "98657.83", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 99668626339273709694",
                "to": "Счет 27219929444683698245",
            },
            {
                "id": 949194534,
                "state": "EXECUTED",
                "date": "2019-08-15T01:48:10.042554",
                "operationAmount": {"amount": "31222.43", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 65298957349197687907",
                "to": "Счет 38784565940893479418",
            },
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            {
                "id": 154927927,
                "state": "EXECUTED",
                "date": "2019-11-19T09:22:25.899614",
                "operationAmount": {"amount": "30153.72", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 7810846596785568",
                "to": "Счет 43241152692663622869",
            },
        ],
        "Перевод организации")
