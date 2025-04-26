import pytest

from src.masks.masks_card import get_mask_card_number


def test_get_mask_card_number(test_number):
    """Тест с использованием фикстуры"""
    assert get_mask_card_number("7000792289606361") == test_number


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063612", "Не верный номер карты"),
        ("700079228960636", "Не верный номер карты"),
        ((), "Не верный номер карты"),
    ],
)
def test_get_mask_card_number_1(number_card, expected):
    """Тест с использованием параметризации"""
    assert get_mask_card_number(number_card) == expected
