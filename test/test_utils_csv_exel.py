import tempfile

from src.utils_csv_exel import read_exel, read_csv


def test_read_exel():
    """Тест функции чтения exel файла на ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as my_file:
        my_file.write(b'my_file.xls')
        result = read_exel(my_file.name)
        assert result == []


def test_read_csv():
    """Тест функции чтения exel файла на ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.write(b'my_file.csv')
        result = read_csv(file.name)
        assert result == []
