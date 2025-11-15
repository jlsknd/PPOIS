class ExpressDelivery:
    """Класс экспресс-доставки."""
    
    def __init__(self, delivery_id, guaranteed_hours):
        """
        Инициализация экспресс-доставки.
        
        Args:
            delivery_id: ID доставки
            guaranteed_hours: Гарантированное время (часы)
        """
        self.delivery_id = delivery_id
        self.guaranteed_hours = guaranteed_hours
        self.surcharge_rate = 0.5  # 50% наценка
        
    def calculate_cost(self, base_cost):
        """Рассчитать стоимость с наценкой."""
        return base_cost * (1 + self.surcharge_rate)
        
    def is_eligible(self, distance_km):
        """Проверить возможность экспресс-доставки."""
        max_distance = self.guaranteed_hours * 80  # 80 км/ч средняя скорость
        return distance_km <= max_distance

