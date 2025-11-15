class Delivery:
    """Класс доставки."""
    
    def __init__(self, delivery_id, shipments, vehicle, driver):
        """
        Инициализация доставки.
        
        Args:
            delivery_id: ID доставки
            shipments: Список грузов
            vehicle: Транспортное средство
            driver: Водитель
        """
        self.delivery_id = delivery_id
        self.shipments = shipments if isinstance(shipments, list) else [shipments]
        self.vehicle = vehicle
        self.driver = driver
        self.route = None
        self.status = "scheduled"
        self.start_time = None
        self.end_time = None
        self.fuel_consumed = 0
        self.delivery_notes = None
        
    def add_shipment(self, shipment):
        """Добавить груз в доставку."""
        self.shipments.append(shipment)
        
    def assign_route(self, route):
        """Назначить маршрут."""
        self.route = route
        
    def start_delivery(self):
        """Начать доставку."""
        self.status = "in_progress"
        self.start_time = datetime.now()
        self.vehicle.set_unavailable()
        for shipment in self.shipments:
            shipment.update_status("in_transit")
            
    def complete_delivery(self):
        """Завершить доставку."""
        self.status = "completed"
        self.end_time = datetime.now()
        self.vehicle.set_available()
        for shipment in self.shipments:
            shipment.mark_delivered()
            
    def get_total_weight(self):
        """Получить общий вес грузов."""
        return sum(s.weight_kg for s in self.shipments)
        
    def get_delivery_duration(self):
        """Получить длительность доставки."""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 3600
        return None

