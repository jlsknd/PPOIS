class Receipt:
    """Класс чека."""
    
    def __init__(self, payment, items):
        """
        Инициализация чека.
        
        Args:
            payment: Платеж
            items: Список позиций
        """
        self.payment = payment
        self.items = items
        self.timestamp = datetime.now()
        self.receipt_number = None
        
    def generate_number(self):
        """Сгенерировать номер чека."""
        self.receipt_number = f"RCP{int(self.timestamp.timestamp())}"
        return self.receipt_number
        
    def get_total(self):
        """Получить общую сумму."""
        return self.payment.get_amount()
        
    def print_receipt(self):
        """Распечатать чек."""
        return f"Чек №{self.receipt_number}\nСумма: {self.get_total()}\nДата: {self.timestamp}"
