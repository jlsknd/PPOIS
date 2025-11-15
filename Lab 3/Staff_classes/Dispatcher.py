class Dispatcher(Employee):
    """Класс диспетчера."""
    
    def __init__(self, employee_id, name, salary):
        """
        Инициализация диспетчера.
        
        Args:
            employee_id: ID диспетчера
            name: Имя
            salary: Зарплата
        """
        super().__init__(employee_id, name, "dispatcher", salary)
        self.assigned_routes = []
        self.calls_handled = 0
        self.shift_start = None
        
    def assign_route(self, route):
        """Назначить маршрут."""
        self.assigned_routes.append(route)
        
    def handle_call(self):
        """Обработать звонок."""
        self.calls_handled += 1
        
    def get_active_routes(self):
        """Получить активные маршруты."""
        return self.assigned_routes
