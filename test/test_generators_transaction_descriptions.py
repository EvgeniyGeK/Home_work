import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Перевод организации"],
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
            ["Перевод со счета на счет"],
        ),
        (
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            ["Перевод с карты на карту"],
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
            [""],
        ),
    ],
)
def test_transaction_descriptions(transactions, expected):
    """Тест с использованием параметризации"""
    test_descriptions = transaction_descriptions(transactions, "descriptions")
    assert list(test_descriptions) == expected
