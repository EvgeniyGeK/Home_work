import pytest
import unittest

from src.generators import filter_by_currency


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
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
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
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions: list[dict], expected: str) -> None:
    """Тест с использованием параметризации"""
    test_transactions = filter_by_currency(transactions, "USD")
    assert list(test_transactions) == expected


def test_filter_by_currency_1(test_filter_currency: list) -> None:
    filtered = filter_by_currency(test_filter_currency, "EUR")
    with pytest.raises(StopIteration):
        next(filtered)




class TestFilterByCurrency(unittest.TestCase):
    def setUp(self):
        self.transactions_direct = [
            {'id': '293898', 'state': 'EXECUTED', 'date': '2023-05-14T18:57:16Z', 'amount': '14031', 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Visa 5962584244183755', 'to': 'Mastercard 8961651103972237', 'description': 'Перевод с карты на карту'},
            {'id': '1849472', 'state': 'EXECUTED', 'date': '2021-09-24T14:59:04Z', 'amount': '21741', 'currency_name': 'Yen', 'currency_code': 'JPY', 'from': 'Visa 6665114452549732', 'to': 'American Express 7292521342622607', 'description': 'Перевод с карты на карту'},
            {'id': '1473389', 'state': 'EXECUTED', 'date': '2023-08-30T00:58:36Z', 'amount': '18420', 'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 3093124722348405', 'to': 'American Express 6950002720800411', 'description': 'Перевод с карты на карту'}
        ]

        self.transactions_nested = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"}
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"}
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ]

    def test_filter_direct_structure(self):
        """Тест на прямую структуру."""
        expected = [{'id': '1473389', 'state': 'EXECUTED', 'date': '2023-08-30T00:58:36Z', 'amount': '18420', 'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 3093124722348405', 'to': 'American Express 6950002720800411', 'description': 'Перевод с карты на карту'}]
        result = list(filter_by_currency(self.transactions_direct, "RUB"))
        self.assertEqual(expected, result)

    def test_filter_nested_structure(self):
        """Тест на вложенную структуру."""
        expected = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
        result = list(filter_by_currency(self.transactions_nested, "RUB"))
        self.assertEqual(expected, result)

    def test_mixed_transactions(self):
        """Тест на смесь прямых и вложенных транзакций."""
        mixed_transactions = self.transactions_direct + self.transactions_nested
        expected = [
            {'id': '1473389', 'state': 'EXECUTED', 'date': '2023-08-30T00:58:36Z', 'amount': '18420', 'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 3093124722348405', 'to': 'American Express 6950002720800411', 'description': 'Перевод с карты на карту'},
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"}
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            }
        ]
        result = list(filter_by_currency(mixed_transactions, "RUB"))
        self.assertEqual(expected, result)

    def test_no_matching_transactions(self):
        """Тест на случай, когда подходящей валюты нет."""
        result = list(filter_by_currency(self.transactions_direct, "AUD"))
        self.assertEqual([], result)

    def test_case_insensitive_comparison(self):
        """Тест на нечувствительность к регистру букв."""
        result = list(filter_by_currency(self.transactions_nested, "rUb"))
        expected = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()


#
