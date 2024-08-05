from unittest.mock import patch

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_additional_product_and_category():
    """Проверяет увеличение количества товаров и категорий при добавлении новых объектов"""
    Category.category_count = 0  # Сброс счетчиков

    # Создаем дополнительные продукты и категории
    product5 = Product("Huawei P50 Pro", "256GB, Черный", 100000.0, 10)
    product6 = Product("Sony Xperia 1", "128GB, Белый", 80000.0, 6)
    category3 = Category("Новые Смартфоны", "Последние модели смартфонов", [product5, product6])

    assert Category.category_count == 1
    assert len(category3.products.split("\n")) == 2


def test_reset_category_and_product_counts():
    """Проверяет сброс счетчиков категорий и продуктов"""
    Category.category_count = 10
    Category.product_count = 50

    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


def test_smartphone_lawn_grass_addition():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    # Тестирование попытки сложения объектов разных типов
    with pytest.raises(TypeError, match="Нельзя сложить объекты разных типов"):
        smartphone + grass


def test_category_product_count(category_smartphones, smartphone3):
    """Проверяет правильность обновления количества продуктов в категории при добавлении нового продукта"""
    with patch("src.main.Category.product_count", new_callable=lambda: 0) as mock_count:
        # Вставляем начальное значение для счетчика
        initial_count = mock_count
        category_smartphones.add_product(smartphone3)
        assert Category.product_count == initial_count + smartphone3.quantity


def test_category_add_non_product(category_smartphones):
    """Проверяет, что попытка добавления не продукта в категорию вызывает исключение TypeError"""
    with pytest.raises(TypeError, match="Можно добавлять только экземпляры класса Product или его наследников"):
        category_smartphones.add_product("Not a product")
