import os

import requests
from dotenv import load_dotenv

from config import PATH

path_to_file = PATH / "data" / "operations.json"

load_dotenv(PATH / ".env")

API_KEY = os.getenv("API_KEY")


def money_transaction(transaction: dict) -> float | str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    try:

        if transaction.get("operationAmount") is not None:
            amount = float(transaction.get("operationAmount").get("amount"))
            currency = transaction.get("operationAmount").get("currency").get("code")
            if currency != "RUB":
                url = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&from&amount={amount}"
                )
                headers = {"apikey": API_KEY}
                response = requests.request("GET", url, headers=headers)
                status_code = response.status_code
                if status_code == 200:
                    result = response.json()
                    return result
                else:
                    return f"Запрос не удался, код ошибки: {status_code}"
            else:
                return amount

    except Exception as error:
        print("Произошла ошибка", error)
        raise Exception
