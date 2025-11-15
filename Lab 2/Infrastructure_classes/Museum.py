class Museum:
    """Класс музея."""
    
    def __init__(self, name, address, capacity):
        """
        Инициализация музея.
        
        Args:
            name: Название музея
            address: Адрес
            capacity: Вместимость
        """
        self.name = name
        self.address = address
        self.capacity = capacity
        self.exhibits = []
        self.visitors_count = 0
        self.is_open = False
        self.opening_hours = {"start": "09:00", "end": "18:00"}
        
    def add_exhibit(self, exhibit):
        """Добавить выставку."""
        self.exhibits.append(exhibit)
        
    def open_museum(self):
        """Открыть музей."""
        self.is_open = True
        for exhibit in self.exhibits:
            exhibit.open_exhibit()
            
    def close_museum(self):
        """Закрыть музей."""
        self.is_open = False
        for exhibit in self.exhibits:
            exhibit.close_exhibit()
            
    def admit_visitor(self, visitor):
        """Впустить посетителя."""
        if not self.is_open:
            raise ExhibitClosedError("Музей закрыт")
        if self.visitors_count >= self.capacity:
            raise CapacityExceededError("Музей полон")
        self.visitors_count += 1
        
    def visitor_exit(self):
        """Посетитель покидает музей."""
        if self.visitors_count > 0:
            self.visitors_count -= 1
            
    def set_opening_hours(self, start, end):
        """Установить часы работы."""
        self.opening_hours = {"start": start, "end": end}
        
    def get_current_capacity(self):
        """Получить текущую заполненность."""
        return self.visitors_count

