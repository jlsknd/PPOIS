class Inventory:
    """Класс управления запасами."""
    
    def __init__(self):
        """Инициализация системы управления запасами."""
        self.items = {}
        self.low_stock_threshold = 10
        
    def add_stock(self, item_id, quantity, item_info):
        """Добавить товар в запасы."""
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
        else:
            self.items[item_id] = {
                'quantity': quantity,
                'info': item_info,
                'last_updated': datetime.now()
            }
            
    def remove_stock(self, item_id, quantity):
        """Убрать товар из запасов."""
        if item_id in self.items and self.items[item_id]['quantity'] >= quantity:
            self.items[item_id]['quantity'] -= quantity
            self.items[item_id]['last_updated'] = datetime.now()
            return True
        return False
        
    def get_stock_level(self, item_id):
        """Получить уровень запасов."""
        return self.items.get(item_id, {}).get('quantity', 0)
        
    def check_low_stock(self):
        """Проверить товары с низким запасом."""
        return [item_id for item_id, data in self.items.items() 
                if data['quantity'] < self.low_stock_threshold]
                
    def get_total_items(self):
        """Получить общее количество товаров."""
        return sum(data['quantity'] for data in self.items.values())
