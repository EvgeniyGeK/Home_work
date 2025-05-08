import pytest

from src.generators import card_number_generator

@pytest.mark.parametrize(
"start, end, expected", [(1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
                         (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"])])

def test_card_number_generator(start: int, end: int, expected) -> None:
    """Тест с использованием параметризации"""
    list_card_number_generator = list(card_number_generator(start, end))
    assert list_card_number_generator == expected
