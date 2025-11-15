class Camera:
    """Класс камеры наблюдения."""
    
    def __init__(self, location, camera_id):
        """
        Инициализация камеры.
        
        Args:
            location: Расположение
            camera_id: ID камеры
        """
        self.location = location
        self.camera_id = camera_id
        self.is_recording = False
        self.footage = []
        
    def start_recording(self):
        """Начать запись."""
        self.is_recording = True
        
    def stop_recording(self):
        """Остановить запись."""
        self.is_recording = False
        
    def save_footage(self, footage_data):
        """Сохранить запись."""
        self.footage.append({
            'data': footage_data,
            'timestamp': datetime.now()
        })
        
    def get_footage(self):
        """Получить записи."""
        return self.footage
