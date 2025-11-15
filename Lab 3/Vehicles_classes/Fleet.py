class Fleet:
    """Класс автопарка."""
    
    def __init__(self, fleet_name):
        """
        Инициализация автопарка.
        
        Args:
            fleet_name: Название автопарка
        """
        self.fleet_name = fleet_name
        self.vehicles = []
        self.total_capacity = 0
        self.fleet_manager = None
        
    def add_vehicle(self, vehicle):
        """Добавить транспорт в парк."""
        self.vehicles.append(vehicle)
        self.total_capacity += vehicle.capacity_kg
        
    def remove_vehicle(self, vehicle):
        """Удалить транспорт из парка."""
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            self.total_capacity -= vehicle.capacity_kg
            
    def get_available_vehicles(self):
        """Получить доступные транспортные средства."""
        return [v for v in self.vehicles if v.is_available]
        
    def find_vehicle_by_capacity(self, required_capacity):
        """Найти транспорт с нужной грузоподъемностью."""
        for vehicle in self.get_available_vehicles():
            if vehicle.get_available_capacity() >= required_capacity:
                return vehicle
        return None
        
    def get_fleet_utilization(self):
        """Получить коэффициент использования парка."""
        if not self.vehicles:
            return 0
        available = len(self.get_available_vehicles())
        return (len(self.vehicles) - available) / len(self.vehicles) * 100
