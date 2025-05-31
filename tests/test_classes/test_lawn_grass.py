import pytest

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_lawn_grass(lawn_grass_test):
    """
    Тестирование объекта `LawnGrass`.

    Assertions:
        - Проверка страны происхождения.
        - Проверка периода прорастания.
        - Проверка цвета травы.
    """
    assert lawn_grass_test.country == "Россия"
    assert lawn_grass_test.germination_period == "14 дней"
    assert lawn_grass_test.color.lower() == "зелёный"


def test_lawn_grass_str(lawn_grass_test):
    """
    Проверяет строковое представление LawnGrass.
    """
    expected = (
        f"{lawn_grass_test.name} ({lawn_grass_test.color}, из {lawn_grass_test.country}) — "
        f"{lawn_grass_test.price} руб., в наличии: {lawn_grass_test.quantity} шт."
    )
    assert str(lawn_grass_test) == expected
