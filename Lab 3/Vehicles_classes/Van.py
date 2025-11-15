class Van(Vehicle):
    """Класс фургона."""
    
    def __init__(self, vehicle_id, capacity_kg):
        """
        Инициализация фургона.
        
        Args:
            vehicle_id: ID фургона
            capacity_kg: Грузоподъемность
        """
        super().__init__(vehicle_id, "van", capacity_kg, "gasoline")
        self.volume_m3 = capacity_kg / 200  # Приблизительный объем
        self.has_hydraulic_lift = False
