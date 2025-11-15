class Building:
    """Класс здания музея."""
    
    def __init__(self, name, floors):
        """
        Инициализация здания.
        
        Args:
            name: Название здания
            floors: Количество этажей
        """
        self.name = name
        self.floors = floors
        self.rooms = []
        self.elevators = []
        
    def add_room(self, room):
        """Добавить комнату."""
        self.rooms.append(room)
        
    def add_elevator(self, elevator):
        """Добавить лифт."""
        self.elevators.append(elevator)
        
    def get_total_rooms(self):
        """Получить общее количество комнат."""
        return len(self.rooms)
