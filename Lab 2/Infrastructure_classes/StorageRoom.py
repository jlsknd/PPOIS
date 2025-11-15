class StorageRoom:
    """Класс хранилища."""
    
    def __init__(self, capacity, security_level):
        """
        Инициализация хранилища.
        
        Args:
            capacity: Вместимость
            security_level: Уровень безопасности
        """
        self.capacity = capacity
        self.security_level = security_level
        self.stored_items = []
        self.is_locked = True
        
    def store_item(self, item):
        """Сохранить предмет."""
        if len(self.stored_items) >= self.capacity:
            raise CapacityExceededError("Хранилище заполнено")
        self.stored_items.append(item)
        return True
        
    def retrieve_item(self, item):
        """Извлечь предмет."""
        if item in self.stored_items:
            self.stored_items.remove(item)
            return item
        return None
        
    def lock(self):
        """Закрыть хранилище."""
        self.is_locked = True
        
    def unlock(self):
        """Открыть хранилище."""
        self.is_locked = False
