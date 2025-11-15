class Product:
    """Класс товара."""
    
    def __init__(self, name, price, category):
        """
        Инициализация товара.
        
        Args:
            name: Название товара
            price: Цена
            category: Категория
        """
        self.name = name
        self.price = price
        self.category = category
        self.description = ""
        
    def set_description(self, description):
        """Установить описание."""
        self.description = description
        
    def apply_discount(self, percentage):
        """Применить скидку."""
        self.price = self.price * (1 - percentage / 100)
        
    def get_price(self):
        """Получить цену."""
        return self.price

