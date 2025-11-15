class SecuritySystem:
    """Класс системы безопасности."""
    
    def __init__(self):
        """Инициализация системы безопасности."""
        self.cameras = []
        self.access_logs = []
        self.is_armed = False
        self.alarm_triggered = False
        
    def add_camera(self, camera):
        """Добавить камеру."""
        self.cameras.append(camera)
        
    def arm_system(self):
        """Активировать систему."""
        self.is_armed = True
        
    def disarm_system(self):
        """Деактивировать систему."""
        self.is_armed = False
        
    def trigger_alarm(self, reason):
        """Включить тревогу."""
        self.alarm_triggered = True
        self.access_logs.append({
            'event': 'alarm',
            'reason': reason,
            'timestamp': datetime.now()
        })
        
    def log_access(self, user_id, location):
        """Записать доступ."""
        self.access_logs.append({
            'user_id': user_id,
            'location': location,
            'timestamp': datetime.now()
        })

