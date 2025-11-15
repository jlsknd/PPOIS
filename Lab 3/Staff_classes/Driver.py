class Driver(Employee):
    """Класс водителя."""
    
    def __init__(self, employee_id, name, salary, license_type):
        """
        Инициализация водителя.
        
        Args:
            employee_id: ID водителя
            name: Имя
            salary: Зарплата
            license_type: Тип лицензии
        """
        super().__init__(employee_id, name, "driver", salary)
        self.license_type = license_type
        self.license_expiry = datetime.now() + timedelta(days=365*5)
        self.assigned_vehicle = None
        self.deliveries_completed = 0
        self.total_distance_km = 0
        self.medical_exam_date = datetime.now()
        self.accident_count = 0
        
    def assign_vehicle(self, vehicle):
        """Назначить транспортное средство."""
        self.assigned_vehicle = vehicle
        
    def complete_delivery(self, distance_km):
        """Завершить доставку."""
        self.deliveries_completed += 1
        self.total_distance_km += distance_km
        
    def is_license_valid(self):
        """Проверить действительность лицензии."""
        return datetime.now() < self.license_expiry
        
    def renew_license(self, years):
        """Продлить лицензию."""
        self.license_expiry = self.license_expiry + timedelta(days=365*years)
