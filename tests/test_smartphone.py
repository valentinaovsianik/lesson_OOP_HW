import pytest
from src.smartphone import Smartphone


def test_smartphone_addition():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    # Ожидаемая сумма стоимости всех смартфонов
    expected_sum = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)

    # Тестирование сложения двух объектов типа Smartphone
    assert smartphone1 + smartphone2 == expected_sum
