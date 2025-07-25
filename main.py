

from config import PATH
from sorted_dict_main import sorted_dict
from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.search_of_dict import process_bank_operations, process_bank_search

from src.utils import read_json_file
from src.utils_csv_exel import read_csv, read_exel


def main():
    # while True:


    try:
        print (f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

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
            print(f"Для обработки выбран JSON-файл.\n")


        elif user_point == "2":
            selected_file = read_csv(PATH / "data" / "transactions.csv")
            print(f"Для обработки выбран CSV-файл.\n")

        elif user_point == "3":
            selected_file = read_exel(PATH / "data" / "transactions_excel.xlsx")
            print(f"Для обработки выбран EXCEL-файл.\n")

        user_filter_status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n").upper()

        if user_filter_status in ["EXECUTED", "CANCELED", "PENDING"] and selected_file is not None:

            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())
            print(f"Операции отфильтрованы по статусу {user_filter_status}")


        else:
            while True:

                print(f"Статус операции {user_filter_status} недоступен.\n"),
                user_filter_status = input(f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n")

                break
            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())
            # print(filter_by_status)
        sorted_transactions = sorted_dict(filter_by_status)

        user_currency = input(f"Выводить только рублевые транзакции? Да/Нет\n").upper()
        if user_currency.startswith("ДА"):
            ruble_transactions = list(filter_by_currency(sorted_transactions, "RUB"))

            output_list = ruble_transactions
            print(output_list)

        else:
            output_list = sorted_transactions
            print(output_list)

        user_description = input(f"Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").upper()
        if user_description.startswith("ДА"):
            user_filter_description = input(f"Введите описание операции по которой необходимо выполнить фильтрацию\n")
            filter_by_word = process_bank_search(output_list, user_filter_description)
            count_transaction = process_bank_operations(filter_by_word, user_filter_description.casefold())
            count_result = next((value for key, value in count_transaction.items() if
                                 key.casefold() == user_filter_description.casefold()), 0)
            print(f"Ключи в count_transaction: {list(count_transaction.keys())}")

            print(f"Распечатываю итоговый список транзакций\n", filter_by_word)
            print(count_transaction)
            print(f'Всего банковских операций в выборке: {count_result}')
        else:
            filter_by_word = output_list
            print(f"Распечатываю итоговый список транзакций\n", filter_by_word)






















    except Exception as e:
        print(e, f"выбран несуществующий пункт меню")
        exit()






    #
    # user_JSON ("1. Получить информацию о транзакциях из JSON-файла. ' '")
    # user_CSV = input ("2. Получить информацию о транзакциях из CSV-файла. ' '")
    # user_XLSX = input("3. Получить информацию о транзакциях из XLSX-файла. ''")
    # if user_JSON:
    #     print("a")
    # elif user_CSV:
    #     print("b")
    # else:
    #     print("c")





if __name__ == "__main__":
    main()