from src.widget import mask_account_card


def print_transactions(transaction: list[dict]) -> None:

    for i in transaction:
        if "Открытие" in i['description']:
            print(f"{i['date']}\n{mask_account_card(i['to'])}\n"
                  f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")

        else:
            print(f"{i['date']}\n{i['description']}\n{mask_account_card(i['from'])} -> {mask_account_card(i['to'])}\n"
                  f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print("")




