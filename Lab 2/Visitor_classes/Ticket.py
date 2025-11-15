class Ticket:
    """Класс билета в музей."""
    
    def __init__(self, ticket_type, price, visitor):
        """
        Инициализация билета.
        
        Args:
            ticket_type: Тип билета
            price: Цена билета
            visitor: Посетитель
        """
        self.ticket_type = ticket_type
        self.price = price
        self.visitor = visitor
        self.purchase_date = datetime.now()
        self.valid_until = datetime.now() + timedelta(days=1)
        self.is_used = False
        self.ticket_number = None
        
    def validate(self):
        """Валидировать билет."""
        if self.is_used:
            raise TicketValidationError("Билет уже использован")
        if datetime.now() > self.valid_until:
            raise TicketValidationError("Билет просрочен")
        return True
        
    def use(self):
        """Использовать билет."""
        self.validate()
        self.is_used = True
        
    def extend_validity(self, days):
        """Продлить срок действия билета."""
        self.valid_until += timedelta(days=days)
        
    def get_price(self):
        """Получить цену билета."""
        return self.price
        
    def is_valid(self):
        """Проверить действительность билета."""
        return not self.is_used and datetime.now() <= self.valid_until

