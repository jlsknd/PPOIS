class Warehouse:
    """Класс склада."""
    
    def __init__(self, warehouse_id, name, location, capacity_m3):
        """
        Инициализация склада.
        
        Args:
            warehouse_id: ID склада
            name: Название
            location: Местоположение
            capacity_m3: Вместимость в м³
        """
        self.warehouse_id = warehouse_id
        self.name = name
        self.location = location
        self.capacity_m3 = capacity_m3
        self.occupied_space = 0.0
        self.inventory = {}
        self.is_climate_controlled = False
        self.temperature_range = None
        self.humidity_level = None
        
    def store_item(self, item_id, item_data):
        """Разместить товар на складе."""
        required_space = item_data.get('volume_m3', 1.0)
        if self.occupied_space + required_space > self.capacity_m3:
            raise InsufficientCapacityError("Недостаточно места на складе")
            
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] += item_data.get('quantity', 1)
        else:
            self.inventory[item_id] = {
                'item_data': item_data,
                'quantity': item_data.get('quantity', 1),
                'stored_at': datetime.now()
            }
        self.occupied_space += required_space
        
    def retrieve_item(self, item_id, quantity=1):
        """Извлечь товар со склада."""
        if item_id not in self.inventory:
            return None
            
        if self.inventory[item_id]['quantity'] >= quantity:
            self.inventory[item_id]['quantity'] -= quantity
            volume = self.inventory[item_id]['item_data'].get('volume_m3', 1.0)
            self.occupied_space -= volume * quantity
            
            if self.inventory[item_id]['quantity'] == 0:
                del self.inventory[item_id]
            return True
        return False
        
    def get_available_space(self):
        """Получить доступное пространство."""
        return self.capacity_m3 - self.occupied_space
        
    def get_occupancy_rate(self):
        """Получить процент заполненности."""
        return (self.occupied_space / self.capacity_m3) * 100 if self.capacity_m3 > 0 else 0
        
    def find_item(self, item_id):
        """Найти товар на складе."""
        return self.inventory.get(item_id)
        
    def get_inventory_count(self):
        """Получить количество позиций."""
        return len(self.inventory)
