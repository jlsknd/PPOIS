class Statistics:
    """Класс статистики."""
    
    def __init__(self):
        """Инициализация статистики."""
        self.metrics = {}
        
    def set_metric(self, name, value):
        """Установить метрику."""
        self.metrics[name] = {
            'value': value,
            'timestamp': datetime.now()
        }
        
    def get_metric(self, name):
        """Получить метрику."""
        return self.metrics.get(name, None)
        
    def calculate_average(self, values):
        """Рассчитать среднее."""
        if not values:
            return 0
        return sum(values) / len(values)
        
    def calculate_growth_rate(self, old_value, new_value):
        """Рассчитать темп роста."""
        if old_value == 0:
            return 0
        return ((new_value - old_value) / old_value) * 100
