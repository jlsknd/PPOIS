class Department:
    """Класс отдела."""
    
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
        self.manager = None
        self.location = None
        self.cost_center = None
        
    def add_employee(self, employee):
        """Добавить сотрудника."""
        self.employees.append(employee)
        employee.assign_department(self)
        
    def remove_employee(self, employee):
        """Удалить сотрудника."""
        if employee in self.employees:
            self.employees.remove(employee)
            
    def assign_manager(self, manager):
        """Назначить менеджера."""
        self.manager = manager
        manager.assign_department(self)
        
    def get_total_payroll(self):
        """Получить общий фонд зарплаты."""
        return sum(emp.salary for emp in self.employees)
        
    def get_employee_count(self):
        """Получить количество сотрудников."""
        return len(self.employees)
