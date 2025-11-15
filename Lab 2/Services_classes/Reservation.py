class Reservation:
    """Класс бронирования."""
    
    def __init__(self, visitor, service, date):
        """
        Инициализация бронирования.
        
        Args:
            visitor: Посетитель
            service: Услуга
            date: Дата
        """
        self.visitor = visitor
        self.service = service
        self.date = date
        self.status = "pending"
        self.confirmation_code = None
        
    def confirm(self):
        """Подтвердить бронирование."""
        self.status = "confirmed"
        self.confirmation_code = f"RES{int(datetime.now().timestamp())}"
        
    def cancel(self):
        """Отменить бронирование."""
        self.status = "cancelled"
        
    def get_status(self):
        """Получить статус."""
        return self.status
