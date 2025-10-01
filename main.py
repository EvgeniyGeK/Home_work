from config import PATH
from src.generators import filter_by_currency
from src.print_transaction_info import print_transactions
from src.processing import filter_by_state
from src.search_of_dict import process_bank_operations, process_bank_search
from src.sorted_dict_main import sorted_dict
from src.utils import read_json_file
from src.utils_csv_exel import read_csv, read_exel


def main():
    """
    Выбор файла с данными
    """

    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

        print("1. Получить информацию о транзакциях из JSON-файла.")
        print("2. Получить информацию о транзакциях из CSV-файла.")
        print("3. Получить информацию о транзакциях из XLSX-файла.")
        print("4. выйти из программы")
        user_point = input("Выберите необходимый пункт меню: ")
        if user_point == "4":
            print("Программа завершена.")
            exit()
        selected_file = None
        if user_point == "1":
            selected_file = read_json_file(PATH / "data" / "operations.json")
            print("Для обработки выбран JSON-файл.\n")

        elif user_point == "2":
            selected_file = read_csv(PATH / "data" / "transactions.csv")
            print("Для обработки выбран CSV-файл.\n")

        elif user_point == "3":
            selected_file = read_exel(PATH / "data" / "transactions_excel.xlsx")
            print("Для обработки выбран EXCEL-файл.\n")
        """
            Фильтрация по статусу
            """
        user_filter_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"
        ).upper()

        if user_filter_status in ["EXECUTED", "CANCELED", "PENDING"] and selected_file is not None:

            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())
            print(f"Операции отфильтрованы по статусу {user_filter_status}")

        else:
            while True:

                print(f"Статус операции {user_filter_status} недоступен.\n"),
                user_filter_status = input(
                    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"
                )

                break
            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())

        sorted_transactions = sorted_dict(filter_by_status)
        """
            Сортировка по валюте
            """
        user_currency = input("Выводить только рублевые транзакции? Да/Нет\n").upper()
        if user_currency.startswith("ДА"):
            ruble_transactions = list(filter_by_currency(sorted_transactions, "RUB"))

            output_list = ruble_transactions

        else:
            output_list = sorted_transactions
            """
                Фильтрация по описанию
                """

        user_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").upper()
        if user_description.startswith("ДА"):
            user_filter_description = input(
                "Введите описание операции по которой необходимо выполнить фильтрацию\n"
            ).upper()

            filter_by_word = process_bank_search(output_list, user_filter_description)
            count_transaction = process_bank_operations(filter_by_word, user_filter_description.casefold())
            count_result = next(
                (
                    value
                    for key, value in count_transaction.items()
                    if key.casefold() == user_filter_description.casefold()
                ),
                0,
            )

            print("Распечатываю итоговый список транзакций\n")

            print(f"Всего банковских операций в выборке: {count_result}")
            print_transactions(filter_by_word)

        else:
            filter_by_word = output_list
            print_transactions(filter_by_word)

    except Exception as e:
        print(e, "выбран несуществующий пункт меню")
        exit()


if __name__ == "__main__":
    main()
