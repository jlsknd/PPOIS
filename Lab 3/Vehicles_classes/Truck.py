class Truck(Vehicle):
    """Класс грузовика."""
    
    def __init__(self, vehicle_id, capacity_kg, has_refrigeration=False):
        """
        Инициализация грузовика.
        
        Args:
            vehicle_id: ID грузовика
            capacity_kg: Грузоподъемность
            has_refrigeration: Наличие рефрижератора
        """
        super().__init__(vehicle_id, "truck", capacity_kg, "diesel")
        self.has_refrigeration = has_refrigeration
        self.trailer_attached = False
        self.axles_count = 3
        self.euro_standard = "EURO-5"
        
    def attach_trailer(self):
        """Прицепить прицеп."""
        self.trailer_attached = True
        self.capacity_kg *= 1.5
        
    def detach_trailer(self):
        """Отцепить прицеп."""
        self.trailer_attached = False
        self.capacity_kg /= 1.5

