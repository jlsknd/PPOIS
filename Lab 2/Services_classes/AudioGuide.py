class AudioGuide:
    """Класс аудиогида."""
    
    def __init__(self, device_id, language):
        """
        Инициализация аудиогида.
        
        Args:
            device_id: ID устройства
            language: Язык
        """
        self.device_id = device_id
        self.language = language
        self.is_available = True
        self.current_user = None
        self.battery_level = 100
        
    def rent(self, visitor):
        """Арендовать аудиогид."""
        if self.is_available:
            self.is_available = False
            self.current_user = visitor
            return True
        return False
        
    def return_device(self):
        """Вернуть устройство."""
        self.is_available = True
        self.current_user = None
        
    def charge(self):
        """Зарядить устройство."""
        self.battery_level = 100
        
    def play_track(self, track_id):
        """Воспроизвести трек."""
        if self.battery_level > 0:
            self.battery_level -= 1
            return f"Воспроизведение трека {track_id}"
        return "Батарея разряжена"
