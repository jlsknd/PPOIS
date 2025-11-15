class Employee:
    """Класс сотрудника музея."""
    
    def __init__(self, name, position, salary):
        """
        Инициализация сотрудника.
        
        Args:
            name: Имя сотрудника
            position: Должность
            salary: Зарплата
        """
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = datetime.now()
        self.is_active = True
        self.department = None
        
    def promote(self, new_position, new_salary):
        """Повысить сотрудника."""
        self.position = new_position
        self.salary = new_salary
        
    def terminate(self):
        """Уволить сотрудника."""
        self.is_active = False
        
    def assign_department(self, department):
        """Назначить отдел."""
        self.department = department
        
    def get_salary(self):
        """Получить зарплату."""
        return self.salary
        
    def calculate_bonus(self, performance_score):
        """Рассчитать бонус."""
        return self.salary * (performance_score / 100) * 0.2
