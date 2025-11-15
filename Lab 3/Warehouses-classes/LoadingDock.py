class LoadingDock:
    """Класс погрузочной платформы."""
    
    def __init__(self, dock_id, max_vehicles):
        """
        Инициализация погрузочной платформы.
        
        Args:
            dock_id: ID платформы
            max_vehicles: Максимальное количество транспорта
        """
        self.dock_id = dock_id
        self.max_vehicles = max_vehicles
        self.current_vehicles = []
        self.is_operational = True
        self.supervisor = None
        
    def assign_vehicle(self, vehicle):
        """Назначить транспорт на платформу."""
        if len(self.current_vehicles) >= self.max_vehicles:
            raise InsufficientCapacityError("Все платформы заняты")
        if not self.is_operational:
            raise InsufficientCapacityError("Платформа не работает")
        self.current_vehicles.append(vehicle)
        
    def release_vehicle(self, vehicle):
        """Освободить транспорт с платформы."""
        if vehicle in self.current_vehicles:
            self.current_vehicles.remove(vehicle)
            
    def get_available_spots(self):
        """Получить количество свободных мест."""
        return self.max_vehicles - len(self.current_vehicles)
        
    def close_dock(self):
        """Закрыть платформу."""
        self.is_operational = False
        
    def open_dock(self):
        """Открыть платформу."""
        self.is_operational = True
