class LogisticsCenter:
    """Класс логистического центра."""
    
    def __init__(self, name, location, capacity):
        """
        Инициализация логистического центра.
        
        Args:
            name: Название
            location: Местоположение
            capacity: Вместимость
        """
        self.name = name
        self.location = location
        self.capacity = capacity
        self.is_operational = False
        self.warehouses = []
        self.loading_docks = []
        self.vehicles_count = 0
        self.operating_hours = {"start": "08:00", "end": "20:00"}
        self.manager = None
        
    def open_center(self):
        """Открыть центр."""
        self.is_operational = True
        
    def close_center(self):
        """Закрыть центр."""
        self.is_operational = False
        
    def add_warehouse(self, warehouse):
        """Добавить склад."""
        self.warehouses.append(warehouse)
        
    def add_loading_dock(self, dock):
        """Добавить погрузочную платформу."""
        self.loading_docks.append(dock)
        
    def set_operating_hours(self, start, end):
        """Установить часы работы."""
        self.operating_hours = {"start": start, "end": end}
        
    def admit_vehicle(self):
        """Впустить транспорт."""
        if not self.is_operational:
            raise InsufficientCapacityError("Центр закрыт")
        if self.vehicles_count >= self.capacity:
            raise InsufficientCapacityError("Центр заполнен")
        self.vehicles_count += 1
        
    def release_vehicle(self):
        """Выпустить транспорт."""
        if self.vehicles_count > 0:
            self.vehicles_count -= 1
