import pytest

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_lawn_grass(lawn_grass_test):
    """
    Тестирование объекта `LawnGrass`.

    Args:
        lawn_grass_test (LawnGrass): Тестовый экземпляр класса `LawnGrass`.

    Assertions:
        - Проверка страны происхождения.
        - Проверка периода прорастания.
        - Проверка цвета травы.
    """
    assert lawn_grass_test.country == "USA"
    assert lawn_grass_test.germination_period == "14 дней"
    assert lawn_grass_test.color == "Зеленый"
