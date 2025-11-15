class Parking:
    """Класс парковки."""
    
    def __init__(self, capacity, hourly_rate):
        """
        Инициализация парковки.
        
        Args:
            capacity: Вместимость
            hourly_rate: Почасовая ставка
        """
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.occupied_spots = 0
        self.vehicles = {}
        
    def park_vehicle(self, vehicle_id):
        """Припарковать автомобиль."""
        if self.occupied_spots >= self.capacity:
            raise CapacityExceededError("Парковка заполнена")
        self.vehicles[vehicle_id] = datetime.now()
        self.occupied_spots += 1
        return True
        
    def remove_vehicle(self, vehicle_id):
        """Убрать автомобиль."""
        if vehicle_id in self.vehicles:
            entry_time = self.vehicles[vehicle_id]
            duration = (datetime.now() - entry_time).seconds / 3600
            fee = duration * self.hourly_rate
            del self.vehicles[vehicle_id]
            self.occupied_spots -= 1
            return fee
        return 0
        
    def get_available_spots(self):
        """Получить количество свободных мест."""
        return self.capacity - self.occupied_spots

