class Department:
    """Класс отдела музея."""
    
    def __init__(self, name, budget):
        """
        Инициализация отдела.
        
        Args:
            name: Название отдела
            budget: Бюджет
        """
        self.name = name
        self.budget = budget
        self.employees = []
        self.head = None
        
    def add_employee(self, employee):
        """Добавить сотрудника."""
        self.employees.append(employee)
        employee.assign_department(self)
        
    def remove_employee(self, employee):
        """Удалить сотрудника."""
        if employee in self.employees:
            self.employees.remove(employee)
            
    def set_head(self, employee):
        """Назначить главу отдела."""
        self.head = employee
        
    def allocate_budget(self, amount):
        """Выделить бюджет."""
        if self.budget >= amount:
            self.budget -= amount
            return True
        return False
        
    def get_employee_count(self):
        """Получить количество сотрудников."""
        return len(self.employees)

