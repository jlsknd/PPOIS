class Transaction:
    """Класс транзакции."""
    
    def __init__(self, from_account, to_account, amount):
        """
        Инициализация транзакции.
        
        Args:
            from_account: Счет отправителя
            to_account: Счет получателя
            amount: Сумма
        """
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.status = "pending"
        self.timestamp = datetime.now()
        self.transaction_type = "transfer"
        
    def execute(self):
        """Выполнить транзакцию."""
        if self.from_account.balance < self.amount:
            self.status = "failed"
            raise InsufficientFundsError("Недостаточно средств")
        
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        self.status = "completed"
        
    def rollback(self):
        """Откатить транзакцию."""
        if self.status == "completed":
            self.to_account.withdraw(self.amount)
            self.from_account.deposit(self.amount)
            self.status = "rolled_back"

