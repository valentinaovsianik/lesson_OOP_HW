class Product:
    """Класс продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info):
        """Создает новый объект Product на основе словаря с параметрами"""
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    """Класс категории продуктов"""

    name: str
    description: str
    products: list[dict]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут для хранения продуктов
        Category.category_count += 1  # Увеличиваем счетчик категорий при создании нового объекта

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем общий счетчик  товаров

    @property
    def products(self):
        """Возвращает список продуктов в виде строки"""
        return "\n".join(str(product) for product in self.__products)


    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    category_count = 0
    product_count = 0


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)