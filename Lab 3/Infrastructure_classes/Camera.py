class Camera:
    """Класс камеры видеонаблюдения."""
    
    def __init__(self, camera_id, location):
        """
        Инициализация камеры.
        
        Args:
            camera_id: ID камеры
            location: Местоположение
        """
        self.camera_id = camera_id
        self.location = location
        self.is_recording = False
        self.footage = []
        
    def start_recording(self):
        """Начать запись."""
        self.is_recording = True
        
    def stop_recording(self):
        """Остановить запись."""
        self.is_recording = False
        
    def save_footage(self, data):
        """Сохранить запись."""
        self.footage.append({
            'data': data,
            'timestamp': datetime.now()
        })

