import json

import pytest

from read_file import open_json

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_open_json_success(mock_json_file):
    # Проверяем корректную загрузку JSON-файла
    result = open_json(str(mock_json_file))
    assert isinstance(result, list)
    assert result == [{"key": "value"}]


def test_open_json_not_found():
    # Проверяем обработку FileNotFoundError
    with pytest.raises(FileNotFoundError):
        open_json("non_existent.json")


def test_open_json_invalid_json(invalid_json_file):
    # Проверяем обработку JSONDecodeError
    with pytest.raises(json.JSONDecodeError):
        open_json(str(invalid_json_file))
