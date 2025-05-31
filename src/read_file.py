from pathlib import Path
import json


def open_json(file_name: str, recursive: bool = False) -> list:
    """Открывает JSON-файл из проекта и возвращает его содержимое.

    Args:
        file_name (str): Имя JSON-файла.
        recursive (bool, optional): Рекурсивный поиск. По умолчанию False.

    Returns:
        list: Содержимое JSON-файла как список.

    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: Если содержимое не является корректным JSON.
    """
    project_root = Path(__file__).resolve().parent.parent
    file_path = find_file(file_name, project_root, recursive)

    try:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Ошибка чтения JSON-файла '{file_name}': {e.msg}", e.doc, e.pos
        ) from e


def find_file(file_name: str, search_dir: Path, recursive: bool = False) -> Path:
    """Ищет файл в указанной директории (с поддержкой рекурсивного поиска).

    Args:
        file_name (str): Имя файла для поиска.
        search_dir (Path): Базовая директория.
        recursive (bool, optional): Поиск во всех подкаталогах. По умолчанию False.

    Returns:
        Path: Путь к найденному файлу.

    Raises:
        FileNotFoundError: Если файл не найден.
    """
    if recursive:
        for file_path in search_dir.rglob(file_name):
            if file_path.is_file():
                return file_path
    else:
        file_path = search_dir / file_name
        if file_path.is_file():
            return file_path

    raise FileNotFoundError(f"Файл '{file_name}' не найден в '{search_dir}'")
