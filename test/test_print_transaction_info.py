from src.print_transaction_info import print_transactions


def test_print_transactions(sample_transactions, capsys):
    expected_output = """\
2019-08-26T10:50:58.294041
Перевод организации
Maestro 1596 83** **** 5199-> Счет **9589
Сумма 31957.58 руб.

2018-03-23T10:45:06.972075
Счет **2431
Сумма 48223.05 руб.\n"""

    print_transactions(sample_transactions)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_transactions_different_types(sample_transactions_diff_type, capsys):
        expected_output = """\
2019-08-26T10:50:58.294041 Перевод организации
Maestro 1596 83** **** 5199-> Счет **9589
Сумма 31957.58 buks

2018-03-23T10:45:06.972075 Открытие вклада
Счет **2431
Сумма 48223.05 euro\n"""

        print_transactions(sample_transactions_diff_type)
        captured = capsys.readouterr()
        assert captured.out == expected_output


def test_print_transactions_exception(invalid_transaction_data, capsys):
    """Тестирует обработку исключения при наличии некорректных данных"""
    print_transactions(invalid_transaction_data)
    captured = capsys.readouterr()
    assert "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации" in captured.out
