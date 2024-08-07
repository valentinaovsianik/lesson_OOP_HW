from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        def __str__(self):
            return (f"{self.name} ({self.color}), Модель: {self.model}, "
                    f"Память: {self.memory} ГБ, {self.price} руб. "
                    f"Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Нельзя сложить объекты разных типов")
