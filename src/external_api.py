import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('APY_KEY')


def money_transaction(transaction: dict) -> [float, str]:
    amount = transaction["operationAmount"],["amount"]
    currency = transaction["operationAmount"], ["currency"], ["code"]
    currency_rub = "RUB"
    if currency != "RUB":
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={currency_rub}from={currency}from&amount={amount}'
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        result = response.json()
        if status_code == 200:
            return result ["result"]
        else:
            return f'Запрос не был успешным. Ошибка {status_code}'
    else:
        return amount