class WarehouseService:
    """Класс складских услуг."""
    
    def __init__(self, daily_rate_per_m3):
        """
        Инициализация складских услуг.
        
        Args:
            daily_rate_per_m3: Дневная ставка за м³
        """
        self.daily_rate_per_m3 = daily_rate_per_m3
        self.stored_items = {}
        
    def store_goods(self, item_id, volume_m3, storage_days):
        """Разместить товары на хранение."""
        self.stored_items[item_id] = {
            'volume_m3': volume_m3,
            'storage_days': storage_days,
            'start_date': datetime.now()
        }
        
    def calculate_storage_cost(self, item_id):
        """Рассчитать стоимость хранения."""
        if item_id in self.stored_items:
            item = self.stored_items[item_id]
            return item['volume_m3'] * self.daily_rate_per_m3 * item['storage_days']
        return 0
        
    def retrieve_goods(self, item_id):
        """Забрать товары со склада."""
        if item_id in self.stored_items:
            del self.stored_items[item_id]
            return True
        return False

