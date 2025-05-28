import json
import os
import requests
from dotenv import load_dotenv
from config import PATH

path_to_file = PATH / "data" / "operations.json"

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


with open(path_to_file, encoding="utf-8") as f:
    transactions = json.load(f)


def money_transaction(transaction: dict, code: str) -> [float, str]:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    try:
        results = []
        for trade in transaction:
            if trade.get("operationAmount") is not None:
                amount = float(trade.get("operationAmount").get("amount"))
                currency = trade.get("operationAmount").get("currency").get("code")
                if currency != "RUB":
                    url = f'https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&from&amount={amount}'
                    payload = {}
                    headers = {"apikey": API_KEY}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    status_code = response.status_code
                    if status_code == 200:
                        result = response.json().get("result")
                        results.append(result)
                    else:
                        return f"Запрос не удался, код ошибки: {status_code}"
                elif currency == code:
                    results.append(amount)

    except Exception as error:
        print("Произошла ошибка", error)
        raise Exception
    return results
