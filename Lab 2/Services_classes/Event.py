class Event:
    """Класс мероприятия."""
    
    def __init__(self, name, event_date, capacity):
        """
        Инициализация мероприятия.
        
        Args:
            name: Название мероприятия
            event_date: Дата мероприятия
            capacity: Вместимость
        """
        self.name = name
        self.event_date = event_date
        self.capacity = capacity
        self.attendees = []
        self.sponsors = []
        
    def register_attendee(self, visitor):
        """Зарегистрировать участника."""
        if len(self.attendees) >= self.capacity:
            raise CapacityExceededError("Мероприятие заполнено")
        self.attendees.append(visitor)
        
    def add_sponsor(self, sponsor):
        """Добавить спонсора."""
        self.sponsors.append(sponsor)
        
    def cancel_event(self):
        """Отменить мероприятие."""
        self.attendees.clear()
        
    def get_attendee_count(self):
        """Получить количество участников."""
        return len(self.attendees)
