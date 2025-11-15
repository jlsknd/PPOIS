class ClimateControl:
    """Класс климат-контроля."""
    
    def __init__(self, target_temp, target_humidity):
        """
        Инициализация климат-контроля.
        
        Args:
            target_temp: Целевая температура
            target_humidity: Целевая влажность
        """
        self.target_temp = target_temp
        self.target_humidity = target_humidity
        self.is_active = False
        
    def activate(self):
        """Активировать климат-контроль."""
        self.is_active = True
        
    def deactivate(self):
        """Деактивировать климат-контроль."""
        self.is_active = False
        
    def adjust_settings(self, temp, humidity):
        """Настроить параметры."""
        self.target_temp = temp
        self.target_humidity = humidity
        
    def monitor_conditions(self, room):
        """Мониторить условия в комнате."""
        status = room.get_climate_status()
        if abs(status['temperature'] - self.target_temp) > 2:
            room.adjust_temperature(self.target_temp)
        if abs(status['humidity'] - self.target_humidity) > 5:
            room.adjust_humidity(self.target_humidity)
