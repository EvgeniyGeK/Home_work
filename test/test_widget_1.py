import pytest

from src.widget import mask_account_card


def test_mask_account_card(test_account_card):
    """Тест с использованием фикстуры"""
    assert mask_account_card("Счет 64686473678894779589") == test_account_card

@pytest.mark.parametrize(
    "number_account, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 70007922896063612", "Не верный номер карты"),
        ("Visa Platinum 700079228960636", "Не верный номер карты"),
        ("", "Не верный номер карты"),
        ]
)
def test_get_mask_account_card_1(number_account, expected):
    """Тест с использованием параметризации"""
    assert mask_account_card(number_account) == expected


