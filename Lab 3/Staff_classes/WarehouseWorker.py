class WarehouseWorker(Employee):
    """Класс складского работника."""
    
    def __init__(self, employee_id, name, salary, shift):
        """
        Инициализация складского работника.
        
        Args:
            employee_id: ID работника
            name: Имя
            salary: Зарплата
            shift: Смена (утренняя, дневная, ночная)
        """
        super().__init__(employee_id, name, "warehouse_worker", salary)
        self.shift = shift
        self.assigned_warehouse = None
        self.items_processed = 0
        self.forklift_certified = False
        self.safety_training_date = None
        
    def assign_warehouse(self, warehouse):
        """Назначить на склад."""
        self.assigned_warehouse = warehouse
        
    def process_items(self, count):
        """Обработать товары."""
        self.items_processed += count
        
    def certify_forklift(self):
        """Получить сертификат на погрузчик."""
        self.forklift_certified = True

