from config import PATH
from src.processing import filter_by_state
from src.search_of_dict import process_bank_search
from src.utils import read_json_file


def main():
    # while True:
    try:
        print (f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

        print("1. Получить информацию о транзакциях из JSON-файла.")
        print("2. Получить информацию о транзакциях из CSV-файла.")
        print("3. Получить информацию о транзакциях из XLSX-файла.")
        print("4. выйти из программы")
        user_point = input("Выберите необходимый пункт меню: ")
        if user_point == "1":
            x = read_json_file(PATH / "data" / "operations.json")
            print(x)
            user_filter_status = input(f"Для обработки выбран JSON-файл.\n" 
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n")
            user_filter_status = user_filter_status.upper()
            if user_filter_status == "EXECUTED" or user_filter_status == "CANCELED" or user_filter_status == "PENDING":
                filter_by_status = filter_by_state(x, user_filter_status)
                print(filter_by_status)
            else:
                print(f"Статус операции {user_filter_status} недоступен.\n"),
                user_filter_status = input  (f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                      f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n")






    except ():
        print(f"выбран несуществующий пункт меню")




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