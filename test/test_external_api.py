import os
import requests
from unittest.mock import patch
import pytest
from src.external_api import money_transaction
import json

with open("test.json", encoding="utf-8") as f:
    test_transactions = json.load(f)
    print(test_transactions)



@patch("requests.get")
def test_money_transaction(mock_get):
    mock_get.return_value.json.return_value = {"result": "31957.58, 688950.806"}
    assert money_transaction(test_transactions, "RUB") == "31957.58, 688950.806"
    # mock_get.assert_called_with(
    #     f"https://api.apilayer.com/exchangerates_data/convert?to='RUB'&from={test_transactions['operationAmount']
    #     ['currency']['code']}&amount={test_transactions['operationAmount']['amount']}"
    # )
