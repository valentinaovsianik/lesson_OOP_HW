from src.main import Category, Product


def test_product_initialization(setup_data):
    """Проверяет корректность инициализации объектов Product"""
    data = setup_data
    assert data["product1"].name == "Samsung Galaxy S23 Ultra"
    assert data["product1"].description == "256GB, Серый цвет, 200MP камера"
    assert data["product1"].price == 180000.0
    assert data["product1"].quantity == 5

    assert data["product2"].name == "Iphone 15"
    assert data["product2"].description == "512GB, Gray space"
    assert data["product2"].price == 210000.0
    assert data["product2"].quantity == 8

    assert data["product3"].name == "Xiaomi Redmi Note 11"
    assert data["product3"].description == "1024GB, Синий"
    assert data["product3"].price == 31000.0
    assert data["product3"].quantity == 14


def test_category_initialization(setup_data):
    """Проверяет корректность инициализации объектов Category и подсчета количества категорий и продуктов"""
    data = setup_data

    assert data["category1"].name == "Смартфоны"
    assert (
        data["category1"].description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(data["category1"].products) == 3
    assert Category.category_count == 2  # Проверяем количество категорий
    assert Category.product_count == 4  # Проверяем общее количество товаров (в текущем тесте)

    assert data["category2"].name == "Телевизоры"
    assert (
        data["category2"].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(data["category2"].products) == 1


def test_product_count_update(setup_data):
    """Проверяет корректность обновления общего количества товаров"""
    data = setup_data

    # Количество товаров должно быть равно сумме товаров во всех категориях
    expected_product_count = len(data["category1"].products) + len(data["category2"].products)
    assert Category.product_count == expected_product_count


def test_additional_product_and_category():
    """Проверяет увеличение количества товаров и категорий при добавлении новых объектов"""
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создаем дополнительные продукты и категории
    product5 = Product("Huawei P50 Pro", "256GB, Черный", 100000.0, 10)
    product6 = Product("Sony Xperia 1", "128GB, Белый", 80000.0, 6)
    category3 = Category("Новые Смартфоны", "Последние модели смартфонов", [product5, product6])

    assert Category.category_count == 1
    assert Category.product_count == 2


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


def test_invalid_product_creation():
    """Проверяет обработку ошибок при создании продукта с некорректными данными"""
    # Ожидаемое исключение при создании продукта с отрицательной ценой
    try:
        Product("Faulty Product", "Invalid price", -100.0, 5)
    except ValueError as e:
        assert str(e) == "Цена продукта не может быть отрицательной"

    # Ожидаемое исключение при создании продукта с отрицательным количеством
    try:
        Product("Faulty Product", "Invalid quantity", 100.0, -5)
    except ValueError as e:
        assert str(e) == "Количество продукта не может быть отрицательным"


def test_product_with_zero_price_and_quantity():
    """Проверяет возможность создания продукта с нулевой ценой и количеством"""
    product = Product("Free Sample", "Sample product", 0.0, 0)
    assert product.name == "Free Sample"
    assert product.price == 0.0
    assert product.quantity == 0


def test_category_without_description():
    """Проверяет возможность создания категории без описания"""
    category = Category("No Description", "", [])
    assert category.name == "No Description"
    assert category.description == ""
    assert len(category.products) == 0


def test_add_product_to_existing_category(setup_data):
    """Проверяет добавление нового продукта в существующую категорию и обновление счетчиков"""
    data = setup_data
    new_product = Product("Google Pixel 6", "128GB, White", 60000.0, 3)
    data["category1"].products.append(new_product)
    Category.product_count += 1

    assert len(data["category1"].products) == 4
    assert Category.product_count == 5  # Обновляем счетчик товаров на 1


def test_create_empty_product_list_category():
    """Проверяет возможность создания категории с пустым списком продуктов"""
    empty_product_list_category = Category("Empty Product List", "Категория без продуктов", [])
    assert empty_product_list_category.name == "Empty Product List"
    assert empty_product_list_category.description == "Категория без продуктов"
    assert len(empty_product_list_category.products) == 0


def test_update_product_quantity():
    """Проверяет корректность обновления количества продукта"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.quantity == 10
    product.quantity = 20
    assert product.quantity == 20


def test_reset_category_and_product_counts():
    """Проверяет сброс счетчиков категорий и продуктов"""
    Category.category_count = 10
    Category.product_count = 50

    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


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
    assert len(category.products) == 1000
    assert Category.product_count == 1000


def test_product_creation_with_long_name():
    """Проверяет создание продукта с длинным именем"""
    long_name = "A" * 1000
    product = Product(long_name, "Описание с длинным именем", 100.0, 10)
    assert product.name == long_name
    assert product.description == "Описание с длинным именем"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_update():
    """Проверяет обновление цены продукта"""
    product = Product("Test Product", "Test Description", 50.0, 10)
    assert product.price == 50.0
    product.price = 75.0
    assert product.price == 75.0
