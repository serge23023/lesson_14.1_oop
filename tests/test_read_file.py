import json
import pytest

from read_file import open_json

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_open_json_success(mock_json_file):
    """
    Тестирование корректной загрузки JSON-файла.

    Args:
        mock_json_file (Path): Временный JSON-файл с корректными данными.

    Assertions:
        - Проверка, что загруженные данные представлены в виде списка.
        - Проверка, что содержимое JSON совпадает с ожидаемыми данными.
    """
    result = open_json(str(mock_json_file))
    assert isinstance(result, list)
    assert result == [{"key": "value"}]


def test_open_json_not_found():
    """
    Тестирование обработки ошибки `FileNotFoundError`.

    Assertions:
        - Проверка, что вызов `open_json` с несуществующим файлом вызывает исключение `FileNotFoundError`.
    """
    with pytest.raises(FileNotFoundError):
        open_json("non_existent.json")


def test_open_json_invalid_json(invalid_json_file):
    """
    Тестирование обработки ошибки `JSONDecodeError`.

    Args:
        invalid_json_file (Path): Временный JSON-файл с некорректными данными.

    Assertions:
        - Проверка, что загрузка некорректного JSON-файла вызывает исключение `JSONDecodeError`.
    """
    with pytest.raises(json.JSONDecodeError):
        open_json(str(invalid_json_file))
