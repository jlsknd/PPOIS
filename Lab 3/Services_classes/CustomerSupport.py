class CustomerSupport:
    """Класс службы поддержки."""
    
    def __init__(self):
        """Инициализация службы поддержки."""
        self.tickets = []
        self.ticket_counter = 0
        
    def create_ticket(self, customer, issue_type, description):
        """Создать тикет."""
        self.ticket_counter += 1
        ticket = {
            'ticket_id': f"TKT{self.ticket_counter:06d}",
            'customer': customer,
            'issue_type': issue_type,
            'description': description,
            'status': 'open',
            'created_at': datetime.now(),
            'resolved_at': None
        }
        self.tickets.append(ticket)
        return ticket
        
    def resolve_ticket(self, ticket_id):
        """Решить тикет."""
        for ticket in self.tickets:
            if ticket['ticket_id'] == ticket_id:
                ticket['status'] = 'resolved'
                ticket['resolved_at'] = datetime.now()
                return True
        return False
        
    def get_open_tickets(self):
        """Получить открытые тикеты."""
        return [t for t in self.tickets if t['status'] == 'open']
