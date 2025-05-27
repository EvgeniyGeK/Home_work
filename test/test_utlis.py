import pytest
import tempfile
from unittest.mock import Mock

from src.utlis import read_json_file


def test_read_json_file():
    """Тест функции чтения json файла на ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'{"key": "value"}')
        result = read_json_file(temp_file.name)
        assert result == []
        