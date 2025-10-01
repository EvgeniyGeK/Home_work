from src.processing import sort_by_date


def sorted_dict(filter_by_status):
    """Функция меню сортировки"""
    while True:
        user_sorted_day = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()

        if user_sorted_day not in ["да", "нет"]:
            print('Некорректный выбор. Пожалуйста, введите "Да" или "Нет".')
            continue

        break

    if user_sorted_day == "да":
        while True:
            user_sort_rank = input("Отсортировать по возрастанию (1) или по убыванию (2)? ").strip()

            if user_sort_rank not in ["1", "2"]:
                print("Некорректный выбор. Выберите между 1 и 2.")
                continue

            break

        if user_sort_rank == "1":
            sorted_result = sort_by_date(filter_by_status, ascending=True)
        else:
            sorted_result = sort_by_date(filter_by_status, ascending=False)

        return sorted_result
    else:
        return filter_by_status
