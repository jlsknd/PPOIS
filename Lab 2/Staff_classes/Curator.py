class Curator:
    """Класс куратора выставки."""
    
    def __init__(self, name, specialization):
        """
        Инициализация куратора.
        
        Args:
            name: Имя куратора
            specialization: Специализация
        """
        self.name = name
        self.specialization = specialization
        self.managed_exhibits = []
        self.experience_years = 0
        
    def manage_exhibit(self, exhibit):
        """Управлять выставкой."""
        self.managed_exhibits.append(exhibit)
        
    def organize_exhibition(self, exhibition):
        """Организовать выставку."""
        return f"Выставка {exhibition.name} организована {self.name}"
        
    def evaluate_artifact(self, artifact):
        """Оценить артефакт."""
        return artifact.value * (1 + self.experience_years * 0.05)
        
    def increase_experience(self, years):
        """Увеличить опыт."""
        self.experience_years += years
