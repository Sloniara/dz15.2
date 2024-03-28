from abc import ABC, abstractmethod

# Абстрактный класс продукта
class AbstractProduct(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    @abstractmethod
    def get_info(self):
        pass

# Класс Продукт
class Product(AbstractProduct):
    def get_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

# Миксин для логирования создания объектов
class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_created_object()

    def log_created_object(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        print(f"Создан объект класса {class_name}: {attributes}")

# Класс Смартфон
class Smartphone(AbstractProduct, LogMixin):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def get_info(self):
        return f"Смартфон: {self.name}, {self.price} руб. Остаток: {self.quantity} шт. Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}"

# Класс Трава газонная
class LawnGrass(AbstractProduct, LogMixin):
    def __init__(self, name, price, quantity, country, germination_period, color):
        super().__init__(name, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        return f"Трава газонная: {self.name}, {self.price} руб. Остаток: {self.quantity} шт. Страна-производитель: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"

# Пример использования
smartphone = Smartphone('iPhone', 1000, 5, 'High', '11 Pro Max', '512GB', 'Space Grey')
lawn_grass = LawnGrass('Райское зело', 50, 20, 'Рай', '14 дней', 'Зеленый')

