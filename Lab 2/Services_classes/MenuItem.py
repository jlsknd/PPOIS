class MenuItem:
    """Класс позиции меню."""
    
    def __init__(self, name, price, category):
        """
        Инициализация позиции меню.
        
        Args:
            name: Название
            price: Цена
            category: Категория
        """
        self.name = name
        self.price = price
        self.category = category
        self.is_available = True
        
    def mark_unavailable(self):
        """Отметить как недоступное."""
        self.is_available = False
        
    def mark_available(self):
        """Отметить как доступное."""
        self.is_available = True
        
    def get_price(self):
        """Получить цену."""
        return self.price

