class TrackingSystem:
    """Класс системы отслеживания."""
    
    def __init__(self):
        """Инициализация системы отслеживания."""
        self.tracked_shipments = {}
        
    def register_shipment(self, shipment):
        """Зарегистрировать груз для отслеживания."""
        if not shipment.tracking_number:
            shipment.assign_tracking_number(f"TRK{len(self.tracked_shipments):08d}")
        self.tracked_shipments[shipment.tracking_number] = shipment
        
    def track_shipment(self, tracking_number):
        """Отследить груз по номеру."""
        if tracking_number in self.tracked_shipments:
            return self.tracked_shipments[tracking_number]
        raise ShipmentNotFoundError(f"Груз с номером {tracking_number} не найден")
        
    def get_shipments_by_status(self, status):
        """Получить грузы по статусу."""
        return [s for s in self.tracked_shipments.values() if s.status == status]
        
    def get_delayed_shipments(self):
        """Получить задержанные грузы."""
        return [s for s in self.tracked_shipments.values() if s.is_delayed()]
        
    def update_shipment_location(self, tracking_number, location):
        """Обновить местоположение груза."""
        shipment = self.track_shipment(tracking_number)
        shipment.update_location(location)
