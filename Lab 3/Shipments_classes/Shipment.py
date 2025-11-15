class Shipment:
    """Класс груза для доставки."""
    
    def __init__(self, shipment_id, sender, recipient, weight_kg, destination):
        """
        Инициализация груза.
        
        Args:
            shipment_id: ID груза
            sender: Отправитель
            recipient: Получатель
            weight_kg: Вес в кг
            destination: Пункт назначения
        """
        self.shipment_id = shipment_id
        self.sender = sender
        self.recipient = recipient
        self.weight_kg = weight_kg
        self.destination = destination
        self.status = "pending"
        self.tracking_number = None
        self.created_at = datetime.now()
        self.estimated_delivery = None
        self.actual_delivery = None
        self.current_location = None
        self.origin = None
        self.priority_level = "normal"
        self.insurance_value = 0
        
    def assign_tracking_number(self, tracking_number):
        """Присвоить трек-номер."""
        self.tracking_number = tracking_number
        
    def update_status(self, new_status):
        """Обновить статус груза."""
        valid_statuses = ["pending", "picked_up", "in_transit", "out_for_delivery", "delivered", "returned"]
        if new_status in valid_statuses:
            self.status = new_status
            
    def set_estimated_delivery(self, delivery_date):
        """Установить предполагаемую дату доставки."""
        self.estimated_delivery = delivery_date
        
    def mark_delivered(self):
        """Отметить как доставлено."""
        self.status = "delivered"
        self.actual_delivery = datetime.now()
        
    def update_location(self, location):
        """Обновить текущее местоположение."""
        self.current_location = location
        
    def calculate_delivery_time(self):
        """Рассчитать время доставки."""
        if self.actual_delivery and self.created_at:
            return (self.actual_delivery - self.created_at).total_seconds() / 3600
        return None
        
    def is_delayed(self):
        """Проверить задержку доставки."""
        if self.estimated_delivery and not self.actual_delivery:
            return datetime.now() > self.estimated_delivery
        return False

