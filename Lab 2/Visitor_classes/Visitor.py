class Visitor:
    """Класс посетителя музея."""
    
    def __init__(self, name, age, email):
        """
        Инициализация посетителя.
        
        Args:
            name: Имя посетителя
            age: Возраст
            email: Email
        """
        self.name = name
        self.age = age
        self.email = email
        self.tickets = []
        self.visit_history = []
        self.loyalty_points = 0
        
    def add_ticket(self, ticket):
        """Добавить билет посетителю."""
        self.tickets.append(ticket)
        
    def record_visit(self, exhibit):
        """Записать посещение выставки."""
        self.visit_history.append({
            'exhibit': exhibit,
            'timestamp': datetime.now()
        })
        self.loyalty_points += 10
        
    def get_active_tickets(self):
        """Получить активные билеты."""
        return [t for t in self.tickets if t.is_valid()]
        
    def get_loyalty_points(self):
        """Получить баллы лояльности."""
        return self.loyalty_points
        
    def redeem_points(self, points):
        """Использовать баллы лояльности."""
        if self.loyalty_points >= points:
            self.loyalty_points -= points
            return True
        return False
