# Менеджер категорий и товаров

## 📑 Содержание

- [Описание](#-описание)
- [Структура классов](#-структура-классов)
  - [Category](#-category)
  - [Product](#-product)
  - [Smartphone](#-smartphone-наследник-product)
  - [LawnGrass](#-lawngrass-наследник-product)
  - [Order](#-order)
  - [MixinLogger](#-mixinlogger)
- [Итератор](#-итератор)
- [Загрузка из JSON](#-загрузка-из-json)
- [Тестирование](#-тестирование)
- [Примеры](#-примеры)
- [Требования](#-требования)
- [Автор](#-автор)

---

## 🧠 Описание

Проект реализует объектно-ориентированную модель магазина с поддержкой:

- Категорий и продуктов
- Заказов
- Расширяемых товаров (смартфоны, газонная трава)
- Итерации по товарам
- Логирования объектов
- Загрузки из JSON
- Полного тестового покрытия

---

## 📚 Структура классов

### 🔹 `Category`
- Описывает категорию товаров
- Связана с одним или несколькими объектами `Product`
- Поддерживает счётчики созданных категорий и уникальных товаров

### 🔹 `Product`
- Базовый класс товара
- Свойства: `name`, `description`, `price`, `quantity`
- Поддерживает сравнение (`__eq__`), сложение (`__add__`)
- Цена защищена геттером/сеттером с валидацией и подтверждением понижения

### 🔹 `Smartphone` (наследник `Product`)
- Дополнительные поля: `efficiency`, `model`, `memory`, `color`

### 🔹 `LawnGrass` (наследник `Product`)
- Дополнительные поля: `country`, `germination_period`, `color`

### 🔹 `Order`
- Представляет заказ на товар
- Рассчитывает `total_cost = quantity × price`
- Проверяет количество (> 0)

### 🔹 `MixinLogger`
- Миксин, логирующий создание объектов через `__repr__()`

---

## 🔄 Итератор

### `ProductIterator`
Позволяет перебирать товары в категории:

```python
for product in ProductIterator(category.products):
    print(product)
```

---

## 📂 Загрузка из JSON

### `read_file.open_json()`
Загружает `products.json`, формирует категории и продукты:

```python
from utils import create_categories

categories = create_categories()
```

---

## 🧪 Тестирование

### 📦 Используются:
- `pytest`
- `pytest-cov`
- `fixtures` (`conftest.py`) для всех сущностей

### 🧪 Покрытие:
```bash
poetry run pytest
```

---

## 🔍 Примеры

### ➕ Создание продукта
```python
product = Product("Телефон", "Модель X", 15000.0, 10)
```

### 🛒 Заказ
```python
order = Order(product, 3)
print(order)  # Заказ: 3 × Телефон на сумму 45000.0 руб.
```

### 📦 Категория
```python
category = Category("Электроника", "Современные гаджеты")
category.add_product(product)
```

---

## ✅ Требования
- Python 3.11+
- pytest
- pytest-cov
### Установка зависимостей:

```bash
poetry install
```