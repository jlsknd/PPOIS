class PackagingService:
    """Класс упаковочных услуг."""
    
    def __init__(self):
        """Инициализация упаковочных услуг."""
        self.packaging_types = {
            'standard': 5.0,
            'fragile': 15.0,
            'hazmat': 25.0,
            'temperature_controlled': 20.0
        }
        
    def calculate_packaging_cost(self, packaging_type, quantity):
        """Рассчитать стоимость упаковки."""
        if packaging_type in self.packaging_types:
            return self.packaging_types[packaging_type] * quantity
        return 0
        
    def add_packaging_type(self, name, price):
        """Добавить тип упаковки."""
        self.packaging_types[name] = price

