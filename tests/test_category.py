import pytest
from src.category import Category
from src.product import Product


def test_category_initialization(setup_data):
    """Проверяет корректность инициализации объекта Category"""
    category = setup_data["category1"]
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_product_count_update(new_setup_data):
    """Проверяет корректность обновления общего количества товаров"""
    data = new_setup_data

    # Получаем список всех продуктов в категориях
    products_in_category1 = data["category1"]._Category__products
    products_in_category2 = data["category2"]._Category__products

    # Подсчитываем общее количество товаров в каждой категории
    total_quantity = sum(product.quantity for product in products_in_category1) + sum(
        product.quantity for product in products_in_category2
    )

    # Проверяем, что общее количество продуктов совпадает с фактическим значением
    assert total_quantity == Category.product_count


def test_empty_category():
    """Проверяет корректность создания категории без продуктов"""
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию без продуктов
    empty_category = Category("Пустая Категория", "Категория без продуктов", [])

    assert empty_category.name == "Пустая Категория"
    assert empty_category.description == "Категория без продуктов"
    assert len(empty_category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_without_description():
    """Проверяет возможность создания категории без описания"""
    category = Category("No Description", "", [])
    assert category.name == "No Description"
    assert category.description == ""
    assert len(category.products) == 0


def test_create_empty_product_list_category():
    """Проверяет возможность создания категории с пустым списком продуктов"""
    empty_product_list_category = Category("Empty Product List", "Категория без продуктов", [])
    assert empty_product_list_category.name == "Empty Product List"
    assert empty_product_list_category.description == "Категория без продуктов"
    assert len(empty_product_list_category.products) == 0


def test_category_description_update():
    """Проверяет обновление описания категории"""
    category = Category("Test Category", "Initial Description", [])
    category.description = "Updated Description"

    assert category.description == "Updated Description"


def test_category_with_large_number_of_products():
    """Проверяет создание категории с большим количеством продуктов"""
    products = [Product(f"Product {i}", "Description", 10.0, 1) for i in range(1000)]
    category = Category("Large Category", "Категория с большим количеством продуктов", products)

    assert category.name == "Large Category"
    assert len(category.products.split("\n")) == 1000


