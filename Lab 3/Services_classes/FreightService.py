class FreightService:
    """Класс услуги грузоперевозок."""
    
    def __init__(self, service_id, service_type, base_rate):
        """
        Инициализация услуги.
        
        Args:
            service_id: ID услуги
            service_type: Тип услуги (domestic, international)
            base_rate: Базовая ставка за кг
        """
        self.service_id = service_id
        self.service_type = service_type
        self.base_rate = base_rate
        self.active_shipments = []
        
    def calculate_cost(self, weight_kg, distance_km):
        """Рассчитать стоимость."""
        base_cost = weight_kg * self.base_rate
        distance_factor = distance_km / 100
        return base_cost * (1 + distance_factor * 0.1)
        
    def add_shipment(self, shipment):
        """Добавить груз."""
        self.active_shipments.append(shipment)
        
    def complete_shipment(self, shipment):
        """Завершить доставку груза."""
        if shipment in self.active_shipments:
            self.active_shipments.remove(shipment)
