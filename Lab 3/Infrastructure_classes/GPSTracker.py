class GPSTracker:
    """Класс GPS-трекера."""
    
    def __init__(self, tracker_id):
        """
        Инициализация GPS-трекера.
        
        Args:
            tracker_id: ID трекера
        """
        self.tracker_id = tracker_id
        self.current_location = None
        self.location_history = []
        self.is_active = True
        
    def update_location(self, latitude, longitude):
        """Обновить местоположение."""
        self.current_location = {
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': datetime.now()
        }
        self.location_history.append(self.current_location)
        
    def get_current_location(self):
        """Получить текущее местоположение."""
        return self.current_location
        
    def get_location_history(self):
        """Получить историю местоположений."""
        return self.location_history
        
    def deactivate(self):
        """Деактивировать трекер."""
        self.is_active = False
