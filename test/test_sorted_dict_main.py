from unittest.mock import patch

from src.sorted_dict_main import sorted_dict


def test_sorted_dict_with_user_input_yes_and_order_1():
    """Проверка корректности обработки выбора пользователя по дате и порядку сортировки"""
    transactions = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "EXECUTED"},
        {"date": "2023-01-03", "state": "EXECUTED"},
    ]

    with patch("builtins.input", side_effect=["да", "1"]):
        result = sorted_dict(transactions)
        dates = [transaction["date"] for transaction in result]
        assert dates == ["2023-01-01", "2023-01-02", "2023-01-03"]


def test_sorted_dict_with_user_input_yes_and_order_2():
    """Проверка корректности обработки выбора пользователя по дате и порядку сортировки по убыванию"""
    transactions = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "EXECUTED"},
        {"date": "2023-01-03", "state": "EXECUTED"},
    ]

    with patch("builtins.input", side_effect=["да", "2"]):
        result = sorted_dict(transactions)
        dates = [transaction["date"] for transaction in result]
        assert dates == ["2023-01-03", "2023-01-02", "2023-01-01"]


def test_sorted_dict_without_sorting():
    """Отказ пользователя от сортировки"""
    transactions = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "EXECUTED"},
        {"date": "2023-01-03", "state": "EXECUTED"},
    ]

    with patch("builtins.input", return_value="нет"):
        result = sorted_dict(transactions)
        assert result == transactions
