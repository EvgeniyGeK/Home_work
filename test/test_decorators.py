import pytest

from src.decorators import log


@log(filename="my_log.txt")
def my_function(x: int, y: int) -> (int, float):
    """Применение декоратора к функции"""
    return x / y


my_function(10, 1)


def test_log_decorators():
    """Тестирование декоратора"""

    @log(filename="my_log.txt")
    def test_log_division(x: int, y: int) -> (int, float):
        return x / y

    result = test_log_division(6, 3)
    assert result == 2


def test_log_decorators_1():
    """Тестирование вывода в консоль"""

    @log(filename="my_log.txt")
    def test_log_division(capsys):
        test_log_division(6, 2)
        captured = capsys.readouterr()
        assert "test_log_division ok" in captured.out


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (5, 6, 11), (0, 0, 0)])
@log(filename="my_log.txt")
def test_log_sum(x, y, expected: int) -> [int]:
    """Тестирование декоратора через параметризацию"""
    sum_result = x + y
    assert sum_result == expected

@log(filename="my_log.txt")
def test_logging_error():
    """Тестирование исключений"""
    with pytest.raises(Exception, match=""):
        my_function(1, 0)
