import json
import pytest
from read_file import open_json, find_file

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_open_json_success(mock_json_file):
    """Проверка корректной загрузки данных из валидного JSON."""
    result = open_json(str(mock_json_file))

    assert isinstance(result, list)
    assert result[0]["name"] == "Электроника"
    assert result[0]["products"][0]["name"] == "iPhone 15"


def test_open_json_not_found():
    """Проверка выброса FileNotFoundError при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        open_json("non_existent.json")


def test_open_json_invalid_json(invalid_json_file):
    """Проверка выброса JSONDecodeError при невалидном содержимом."""
    with pytest.raises(json.JSONDecodeError):
        open_json(str(invalid_json_file))


def test_find_file_recursive(tmp_path):
    """
    Проверяет рекурсивный поиск файла через find_file().
    """
    nested = tmp_path / "deep"
    nested.mkdir()

    target = nested / "target.json"
    target.write_text("[]", encoding="utf-8")

    result = find_file("target.json", search_dir=tmp_path, recursive=True)

    assert result.name == "target.json"
    assert result.is_file()
    assert result.parent == nested


def test_find_file_recursive_not_found(tmp_path):
    """
    Проверка FileNotFoundError при рекурсивном поиске несуществующего файла.
    """
    with pytest.raises(FileNotFoundError):
        find_file("does_not_exist.json", search_dir=tmp_path, recursive=True)
