import io
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from src.utils_csv_exel import read_csv, read_exel


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


class TestReadExel(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_exel_success(self, mock_read_excel):
        """Тест на чтение excel файлов функцией read_exel"""
        df_mock = pd.DataFrame({"Name": ["Alice"], "Age": [25]})
        mock_read_excel.return_value = df_mock
        path_to_file = "test.xlsx"
        result = read_exel(path_to_file)
        expected_result = [{"Name": "Alice", "Age": 25}]
        self.assertEqual(result, expected_result)

    @patch("pandas.read_excel")
    def test_read_exel_failure(self, mock_read_excel):
        """Тест на ошибку функцией read_exel"""
        mock_read_excel.side_effect = FileNotFoundError("Файл не найден")
        path_to_file = "nonexistent_file.xlsx"
        result = read_exel(path_to_file)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()


class TestReadCsv(unittest.TestCase):

    @patch("builtins.open")
    def test_read_csv_success(self, mock_open):
        """Тест на чтение csv файлов функцией read_csv"""
        fake_csv_content = """Name;Age\nJohn;30\nJane;25"""
        mock_open.return_value.__enter__.return_value = io.StringIO(fake_csv_content)
        path_to_file = "fake.csv"
        result = read_csv(path_to_file)
        expected_result = [{"Name": "John", "Age": "30"}, {"Name": "Jane", "Age": "25"}]
        self.assertEqual(result, expected_result)

    @patch("builtins.open")
    def test_read_csv_error(self, mock_open):
        """Тест на ошибку функцией read_csv"""
        mock_open.side_effect = IOError("File not found")
        path_to_file = "invalid_path.csv"
        result = read_csv(path_to_file)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
