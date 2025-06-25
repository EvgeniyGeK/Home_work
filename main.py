

from config import PATH
from sorted_dict_main import sorted_dict
from src.processing import filter_by_state

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
            print(f"Для обработки выбран JSON-файл.\n", selected_file)


        elif user_point == "2":
            selected_file = read_csv(PATH / "data" / "transactions.csv")
            print(f"Для обработки выбран CSV-файл.\n", selected_file)

        elif user_point == "3":
            selected_file = read_exel(PATH / "data" / "transactions_excel.xlsx")
            print(f"Для обработки выбран EXCEL-файл.\n", selected_file)

        user_filter_status = (input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"))

        if user_filter_status.upper() in ["EXECUTED", "CANCELED", "PENDING"] and selected_file is not None:
            # filter_dc = filter_by_state(selected_file, user_filter_status.upper())
            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())
            print(filter_by_status)


        else:
            while True:

                print(f"Статус операции {user_filter_status} недоступен.\n"),
                user_filter_status = input(f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n")

                break
            filter_by_status = filter_by_state(selected_file, user_filter_status.upper())
            print(filter_by_status)
        print(sorted_dict(filter_by_status))



















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