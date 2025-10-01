from collections import Counter

from src.search_of_dict import process_bank_operations


def test_fnk_bank_operation(test_search_str, test_process_bank_operations):
    assert process_bank_operations(test_search_str, test_process_bank_operations) == Counter(
        {"Перевод организации": 1, "Перевод с карты на счет": 1, "Перевод с карты на карту": 1}
    )
