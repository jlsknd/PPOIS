class Vehicle:
    """Класс транспортного средства."""
    
    def __init__(self, vehicle_id, vehicle_type, capacity_kg, fuel_type):
        """
        Инициализация транспортного средства.
        
        Args:
            vehicle_id: ID транспортного средства
            vehicle_type: Тип (грузовик, фургон, контейнеровоз)
            capacity_kg: Грузоподъемность в кг
            fuel_type: Тип топлива
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity_kg = capacity_kg
        self.fuel_type = fuel_type
        self.current_load = 0.0
        self.is_available = True
        self.mileage = 0
        self.last_maintenance = datetime.now()
        self.location = None
        self.license_plate = None
        self.vin_number = None
        self.insurance_expiry = None
        self.fuel_tank_capacity = 0
        self.current_fuel_level = 0
        
    def load_cargo(self, weight):
        """Загрузить груз."""
        if not self.is_available:
            raise VehicleUnavailableError("Транспорт недоступен")
        if self.current_load + weight > self.capacity_kg:
            raise OverweightError(f"Превышен допустимый вес на {self.current_load + weight - self.capacity_kg} кг")
        self.current_load += weight
        
    def unload_cargo(self, weight):
        """Выгрузить груз."""
        if weight > self.current_load:
            weight = self.current_load
        self.current_load -= weight
        
    def set_unavailable(self):
        """Сделать транспорт недоступным."""
        self.is_available = False
        
    def set_available(self):
        """Сделать транспорт доступным."""
        self.is_available = True
        
    def schedule_maintenance(self):
        """Запланировать обслуживание."""
        self.is_available = False
        return datetime.now() + timedelta(days=1)
        
    def complete_maintenance(self):
        """Завершить обслуживание."""
        self.last_maintenance = datetime.now()
        self.is_available = True
        
    def add_mileage(self, kilometers):
        """Добавить пробег."""
        self.mileage += kilometers
        
    def get_available_capacity(self):
        """Получить доступную грузоподъемность."""
        return self.capacity_kg - self.current_load

