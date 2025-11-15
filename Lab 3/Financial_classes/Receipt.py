class Receipt:
    """Класс квитанции."""
    
    def __init__(self, payment, customer):
        """
        Инициализация квитанции.
        
        Args:
            payment: Платеж
            customer: Клиент
        """
        self.payment = payment
        self.customer = customer
        self.receipt_number = None
        self.issue_date = datetime.now()
        
    def generate_number(self):
        """Сгенерировать номер квитанции."""
        self.receipt_number = f"RCP{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
    def get_total(self):
        """Получить итоговую сумму."""
        return self.payment.amount
