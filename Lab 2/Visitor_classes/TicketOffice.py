class TicketOffice:
    """Класс кассы для продажи билетов."""
    
    def __init__(self, museum):
        """
        Инициализация кассы.
        
        Args:
            museum: Музей
        """
        self.museum = museum
        self.sold_tickets = []
        self.revenue = 0.0
        self.is_open = True
        
    def sell_ticket(self, ticket_type, visitor, payment):
        """
        Продать билет.
        
        Args:
            ticket_type: Тип билета
            visitor: Посетитель
            payment: Платеж
        """
        if not self.is_open:
            raise TicketValidationError("Касса закрыта")
            
        ticket = Ticket(ticket_type, payment.amount, visitor)
        ticket.ticket_number = f"TKT{len(self.sold_tickets):06d}"
        
        visitor.add_ticket(ticket)
        self.sold_tickets.append(ticket)
        self.revenue += payment.amount
        
        return ticket
        
    def refund_ticket(self, ticket):
        """Вернуть билет."""
        if ticket.is_used:
            raise TicketValidationError("Использованный билет нельзя вернуть")
        self.revenue -= ticket.price
        return ticket.price
        
    def open_office(self):
        """Открыть кассу."""
        self.is_open = True
        
    def close_office(self):
        """Закрыть кассу."""
        self.is_open = False
        
    def get_daily_revenue(self):
        """Получить дневную выручку."""
        return self.revenue
