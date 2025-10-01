from collections import Counter

import pytest

from src.search_of_dict import process_bank_operations



@pytest.mark.parametrize("categories, expected_result", [
    ("Перевод организации, Открытие вклада",
     Counter({"Перевод организации": 1, "Открытие вклада": 1}))
])
def test_process_bank_operations(bank_operations, categories, expected_result):
    result = process_bank_operations(bank_operations, categories)
    assert result == expected_result