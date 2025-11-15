class Payment:
    """Класс платежа."""
    
    def __init__(self, amount, payment_method, description=""):
        """
        Инициализация платежа.
        
        Args:
            amount: Сумма платежа
            payment_method: Способ оплаты
            description: Описание платежа
        """
        self.amount = amount
        self.payment_method = payment_method
        self.description = description
        self.timestamp = datetime.now()
        self.status = "pending"
        self.transaction_id = None
        
    def process(self):
        """Обработать платеж."""
        self.status = "processing"
        return True
        
    def complete(self, transaction_id):
        """Завершить платеж."""
        self.status = "completed"
        self.transaction_id = transaction_id
        
    def cancel(self):
        """Отменить платеж."""
        self.status = "cancelled"
        
    def get_status(self):
        """Получить статус платежа."""
        return self.status
        
    def get_amount(self):
        """Получить сумму платежа."""
        return self.amount

