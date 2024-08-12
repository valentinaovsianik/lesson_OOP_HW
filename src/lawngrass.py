from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.color}), {self.price} руб. "
            f"Страна: {self.country}, Период всходов: {self.germination_period} дней, "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Нельзя сложить объекты разных типов")
