class Payment:
    """Класс платежа."""
    
    def __init__(self, amount, payment_method, description):
        """
        Инициализация платежа.
        
        Args:
            amount: Сумма
            payment_method: Способ оплаты
            description: Описание
        """
        self.amount = amount
        self.payment_method = payment_method
        self.description = description
        self.status = "pending"
        self.timestamp = datetime.now()
        self.transaction_id = None
        self.currency = "RUB"
        
    def process(self):
        """Обработать платеж."""
        self.status = "processing"
        
    def complete(self):
        """Завершить платеж."""
        self.status = "completed"
        
    def cancel(self):
        """Отменить платеж."""
        self.status = "cancelled"
        
    def get_amount(self):
        """Получить сумму платежа."""
        return self.amount
