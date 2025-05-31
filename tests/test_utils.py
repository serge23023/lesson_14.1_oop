from classes.Order_Classes.category import Category
from utils import create_categories
from read_file import open_json


def test_create_categories_returns_categories(mock_json_file, monkeypatch):
    """Проверяет, что create_categories возвращает список объектов Category."""

    monkeypatch.setattr("utils.open_json", lambda *args, **kwargs: open_json(mock_json_file))

    categories = create_categories()
    assert isinstance(categories, list)
    assert all(isinstance(cat, Category) for cat in categories)
    assert categories  # Проверка, что список не пустой
