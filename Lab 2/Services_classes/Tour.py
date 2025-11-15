class Tour:
    """Класс экскурсии."""
    
    def __init__(self, title, duration, max_participants):
        """
        Инициализация экскурсии.
        
        Args:
            title: Название экскурсии
            duration: Продолжительность
            max_participants: Максимальное количество участников
        """
        self.title = title
        self.duration = duration
        self.max_participants = max_participants
        self.participants = []
        self.guide = None
        self.scheduled_time = None
        
    def add_participant(self, visitor):
        """Добавить участника."""
        if len(self.participants) >= self.max_participants:
            raise CapacityExceededError("Экскурсия заполнена")
        self.participants.append(visitor)
        
    def assign_guide(self, guide):
        """Назначить гида."""
        self.guide = guide
        
    def schedule(self, time):
        """Запланировать экскурсию."""
        self.scheduled_time = time
        
    def start_tour(self):
        """Начать экскурсию."""
        if self.guide:
            return self.guide.conduct_tour(self)
        return None
