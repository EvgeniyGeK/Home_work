import pytest

from src.masks.masks_card import get_mask_account


def test_get_mask_account(test_account):
    """Тест с использованием фикстуры"""
    assert get_mask_account("73654108430135874305") == test_account


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587430", "Не верный номер счета"),
        ("736541084301358743052", "Не верный номер счета"),
        ("", "Не верный номер счета"),
    ],
)
def test_get_mask_account_1(account_number, expected):
    """Тест с использованием параметризации"""
    assert get_mask_account(account_number) == expected
