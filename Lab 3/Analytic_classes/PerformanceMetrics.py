class PerformanceMetrics:
    """Класс метрик производительности."""
    
    def __init__(self):
        """Инициализация метрик."""
        self.metrics = {}
        
    def set_metric(self, name, value):
        """Установить метрику."""
        self.metrics[name] = {
            'value': value,
            'timestamp': datetime.now()
        }
        
    def get_metric(self, name):
        """Получить метрику."""
        return self.metrics.get(name, {}).get('value')
        
    def calculate_average_delivery_time(self, delivery_times):
        """Рассчитать среднее время доставки."""
        if not delivery_times:
            return 0
        return sum(delivery_times) / len(delivery_times)
        
    def calculate_vehicle_utilization(self, total_vehicles, active_vehicles):
        """Рассчитать использование транспорта."""
        if total_vehicles == 0:
            return 0
        return (active_vehicles / total_vehicles) * 100
