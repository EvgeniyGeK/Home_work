from unittest.mock import patch, MagicMock
import pytest
from src import external_api


@patch("requests.request")
def test_money_transaction_rub(mock_get):
    expected = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    assert external_api.money_transaction(expected) == 31957.58


@patch("requests.request")
def test_money_transaction_usd(mock_get):
    expected = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = 700000.00
    amount = float(expected.get("operationAmount").get("amount"))
    currency = expected.get("operationAmount").get("currency").get("code")
    assert external_api.money_transaction(expected) == 700000.00
    mock_get.assert_called_once_with(
        "GET",
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&from&amount={amount}",
        headers={"apikey": "COQsTzuTVQihyM5tKWbURoIlccPu7lAn"},
    )
