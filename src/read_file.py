from pathlib import Path
import json


def open_json(file_name: str, recursive: bool = False) -> list:
    """
    Открывает JSON-файл, начиная поиск от корневой директории проекта.

    Args:
        file_name (str): Название файла.
        recursive (bool, optional): Определяет, искать ли файл рекурсивно в подкаталогах. По умолчанию False.

    Returns:
        list: Содержимое JSON-файла.

    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: Если файл не является корректным JSON.
    """
    # Определяем корневую директорию проекта
    project_root = Path(__file__).resolve().parent.parent

    # Выполняем поиск файла
    file_path = find_file(file_name, project_root, recursive)

    try:
        # Открываем файл и читаем содержимое
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка обработки JSON-файла '{file_name}': {e}", e.doc, e.pos) from e


def find_file(filename: str, search_dir: Path, recursive: bool = False) -> Path:
    """
    Находит файл в указанной директории или её подкаталогах.

    Args:
        filename (str): Название файла.
        search_dir (Path): Директория для поиска.
        recursive (bool, optional): Рекурсивно искать файл в подкаталогах. По умолчанию False.

    Returns:
        Path: Объект Path к найденному файлу.

    Raises:
        FileNotFoundError: Если файл не найден.
    """
    if recursive:
        # Рекурсивный поиск файла
        for file_path in search_dir.rglob(filename):
            return file_path
    else:
        # Поиск только в указанной директории
        filepath = search_dir / filename
        if filepath.exists():
            return filepath

    raise FileNotFoundError(f"Файл '{filename}' не найден в директории '{search_dir}'")
