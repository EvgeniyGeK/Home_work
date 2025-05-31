import os
import requests
from unittest.mock import patch, MagicMock
import pytest
from src.external_api import money_transaction, transactions
import json


@patch("requests.request")
def test_money_transaction(mock_get):
    expected = [
  {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected
    assert money_transaction(expected, "RUB") == expected
    # mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={"currency"}&from&amount={"test_amount"}')

