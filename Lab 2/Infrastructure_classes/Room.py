class Room:
    """Класс комнаты в музее."""
    
    def __init__(self, room_number, floor, area):
        """
        Инициализация комнаты.
        
        Args:
            room_number: Номер комнаты
            floor: Этаж
            area: Площадь
        """
        self.room_number = room_number
        self.floor = floor
        self.area = area
        self.temperature = 20.0
        self.humidity = 50.0
        self.is_climate_controlled = True
        
    def adjust_temperature(self, new_temp):
        """Настроить температуру."""
        self.temperature = new_temp
        
    def adjust_humidity(self, new_humidity):
        """Настроить влажность."""
        self.humidity = new_humidity
        
    def get_climate_status(self):
        """Получить статус климата."""
        return {
            'temperature': self.temperature,
            'humidity': self.humidity
        }


