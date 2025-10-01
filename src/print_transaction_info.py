from src.widget import mask_account_card


def print_transactions(transaction: list[dict]) -> None:
    """Функция вывода запрашиваемой информации"""
    try:

        for i in transaction:
            if "operationAmount" in i and isinstance(i["operationAmount"], dict):
                if "Открытие" in i["description"]:
                    print(
                        f"{i['date']} {i['description']}\n{mask_account_card(i['to'])}\n"
                        f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
                    )

                else:
                    print(
                        f"{i['date']} {i['description']}\n{mask_account_card(i['from'])}"
                        f"-> {mask_account_card(i['to'])}\n"
                        f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
                    )
                    print("")
            else:
                if "Открытие" in i["description"]:
                    print(
                        f"{i['date']} {i['description']}\n{mask_account_card(i['to'])}\n"
                        f"Сумма {i['amount']} {i['currency_name']}"
                    )

                else:
                    print(
                        f"{i['date']} {i['description']}\n{mask_account_card(i['from'])}"
                        f"-> {mask_account_card(i['to'])}\n"
                        f"Сумма {i['amount']} {i['currency_name']}"
                    )
                    print("")
    except Exception as e:
        print(e, "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
