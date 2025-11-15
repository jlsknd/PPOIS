class SecuritySystem:
    """Класс системы безопасности."""
    
    def __init__(self):
        """Инициализация системы безопасности."""
        self.cameras = []
        self.alarms = []
        self.is_armed = False
        self.access_logs = []
        
    def add_camera(self, camera):
        """Добавить камеру."""
        self.cameras.append(camera)
        
    def arm_system(self):
        """Включить систему."""
        self.is_armed = True
        
    def disarm_system(self):
        """Выключить систему."""
        self.is_armed = False
        
    def trigger_alarm(self, reason):
        """Активировать тревогу."""
        alarm = {
            'reason': reason,
            'timestamp': datetime.now(),
            'status': 'active'
        }
        self.alarms.append(alarm)
        
    def log_access(self, user, location):
        """Записать доступ."""
        self.access_logs.append({
            'user': user,
            'location': location,
            'timestamp': datetime.now()
        })
        
    def get_recent_alarms(self):
        """Получить последние тревоги."""
        return [a for a in self.alarms if a['status'] == 'active']
