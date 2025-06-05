import tempfile
from unittest import mock
from unittest.mock import patch

from src.utils_csv_exel import read_exel, read_csv


def test_read_exel():
    """Тест функции чтения exel файла на ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as my_file:
        my_file.write(b"my_file.xls")
        result = read_exel(my_file.name)
        assert result == []


def test_read_csv():
    """Тест функции чтения csv файла на ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.write(b"my_file.csv")
        result = read_csv(file.name)
        assert result == []


# @patch("builtins.open")
@patch("pandas.read_excel")
def test_read_exel_path(mock_read_excel):
    """Тест для функции чтения json файла"""
    mock_file = mock.MagicMock()
    # mock_open.return_value.__enter__.return_value = mock_file
    mock_read_excel.return_value = [
        {
            "id": "650703.0",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210.0",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert read_exel(mock_file) == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read_excel.assert_called_with(mock_file)
