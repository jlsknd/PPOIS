class StorageZone:
    """Класс зоны хранения."""
    
    def __init__(self, zone_id, zone_type, capacity):
        """
        Инициализация зоны хранения.
        
        Args:
            zone_id: ID зоны
            zone_type: Тип (ambient, refrigerated, frozen, hazmat)
            capacity: Вместимость
        """
        self.zone_id = zone_id
        self.zone_type = zone_type
        self.capacity = capacity
        self.items = []
        self.temperature = None
        self.warehouse = None
        
    def add_item(self, item):
        """Добавить товар в зону."""
        if len(self.items) >= self.capacity:
            raise InsufficientCapacityError("Зона заполнена")
        self.items.append(item)
        
    def remove_item(self, item):
        """Удалить товар из зоны."""
        if item in self.items:
            self.items.remove(item)
            
    def set_temperature(self, temperature):
        """Установить температуру."""
        self.temperature = temperature
        
    def is_full(self):
        """Проверить заполненность зоны."""
        return len(self.items) >= self.capacity
