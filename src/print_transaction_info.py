def print_transactions(transaction: list[dict]) -> None:

    for i in transaction:
        if "Открытие" in i['description']:
            print(f"{i['date']}\n{i['to']}\n"
                  f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        else:
            print(f"{i['date']}\n{i['description']}\n{i['from']} -> {i['to']}\n"
                  f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")