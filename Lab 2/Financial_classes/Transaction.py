class Transaction:
    """Класс транзакции."""
    
    def __init__(self, from_account, to_account, amount):
        """
        Инициализация транзакции.
        
        Args:
            from_account: Счет отправителя
            to_account: Счет получателя
            amount: Сумма транзакции
        """
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.timestamp = datetime.now()
        self.status = "pending"
        
    def execute(self):
        """Выполнить транзакцию."""
        try:
            self.from_account.withdraw(self.amount)
            self.to_account.deposit(self.amount)
            self.status = "completed"
            return True
        except Exception as e:
            self.status = "failed"
            raise PaymentProcessingError(f"Ошибка транзакции: {str(e)}")
            
    def rollback(self):
        """Откатить транзакцию."""
        if self.status == "completed":
            self.to_account.withdraw(self.amount)
            self.from_account.deposit(self.amount)
            self.status = "rolled_back"
            
    def get_status(self):
        """Получить статус транзакции."""
        return self.status

