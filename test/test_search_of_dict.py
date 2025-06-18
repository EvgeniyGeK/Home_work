import pytest


from src.search_of_dict import process_bank_search
from test.conftest import test_search_bar


def test_get_process_bank_search(test_search_str, test_search_bar):
    """Тест функции поиска по строке в банковских транзакциях"""
    assert process_bank_search(test_search_str, test_search_bar) == [
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
                "description": "Перевод с карты на счет",
            }]

def test_user_search(test_search_str, test_search_user_request):
    """Тест функции поиска по строке в банковских транзакциях в зависимости от регистра ввода"""
    assert process_bank_search(test_search_str, test_search_user_request) == [{
                "id": 593027.0,
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": 30368.0,
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            }
        ]




