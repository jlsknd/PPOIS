class VisitorGroup:
    """Класс группы посетителей."""
    
    def __init__(self, group_name, max_size):
        """
        Инициализация группы.
        
        Args:
            group_name: Название группы
            max_size: Максимальный размер
        """
        self.group_name = group_name
        self.max_size = max_size
        self.members = []
        self.guide = None
        
    def add_member(self, visitor):
        """Добавить участника в группу."""
        if len(self.members) >= self.max_size:
            raise CapacityExceededError("Группа полная")
        self.members.append(visitor)
        
    def remove_member(self, visitor):
        """Удалить участника из группы."""
        if visitor in self.members:
            self.members.remove(visitor)
            
    def assign_guide(self, guide):
        """Назначить гида."""
        self.guide = guide
        
    def get_size(self):
        """Получить размер группы."""
        return len(self.members)
        
    def is_full(self):
        """Проверить заполненность группы."""
        return len(self.members) >= self.max_size
