import pytest

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_smartphone(smartphone_test):
    """
    Тестирование объекта `Smartphone`.

    Assertions:
        - Проверка уровня эффективности.
        - Проверка модели смартфона.
        - Проверка объёма памяти.
        - Проверка цвета устройства.
    """
    assert smartphone_test.efficiency == "A++"
    assert smartphone_test.model == "SM-12345"
    assert smartphone_test.memory == "512GB"
    assert smartphone_test.color.lower() == "чёрный"


def test_smartphone_str(smartphone_test):
    """
    Проверка строкового представления `Smartphone`.

    Assertions:
        - Проверяет формат строки, возвращаемой __str__().
    """
    expected = (
        f"{smartphone_test.name} "
        f"({smartphone_test.model}, {smartphone_test.memory}, {smartphone_test.color}) — "
        f"{smartphone_test.price} руб., в наличии: {smartphone_test.quantity} шт."
    )
    assert str(smartphone_test) == expected
