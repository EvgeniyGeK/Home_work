import tempfile
from typing import Any
from unittest import mock
from unittest.mock import patch

from src.utils import read_json_file


def test_read_json_file():
    """Тест функции чтения json файла на ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'{"key": "value"}')
        result = read_json_file(temp_file.name)
        assert result == []


def test_read_file(test_utils_1: Any) -> None:
    """Тест для функции чтения json файла"""
    assert read_json_file(test_utils_1) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


@patch("builtins.open")
@patch("json.load")
def test_read_file_path(mock_load, mock_open):
    """Тест для функции чтения json файла"""
    mock_file = mock.MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file
    mock_load.return_value = [{"test": "test"}]
    assert read_json_file("fake_path.json") == [{"test": "test"}]
    mock_load.assert_called_with(mock_file)
