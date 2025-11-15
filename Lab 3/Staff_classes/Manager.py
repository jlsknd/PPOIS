class Manager(Employee):
    """Класс менеджера."""
    
    def __init__(self, employee_id, name, salary, team_size):
        """
        Инициализация менеджера.
        
        Args:
            employee_id: ID менеджера
            name: Имя
            salary: Зарплата
            team_size: Размер команды
        """
        super().__init__(employee_id, name, "manager", salary)
        self.team_size = team_size
        self.team_members = []
        self.projects_completed = 0
        self.performance_rating = 0
        
    def add_team_member(self, employee):
        """Добавить члена команды."""
        if len(self.team_members) < self.team_size:
            self.team_members.append(employee)
            employee.assign_department(self.department)
            
    def remove_team_member(self, employee):
        """Удалить члена команды."""
        if employee in self.team_members:
            self.team_members.remove(employee)
            
    def complete_project(self):
        """Завершить проект."""
        self.projects_completed += 1
