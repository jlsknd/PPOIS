class Account:
    """Класс счета."""
    
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        """
        Инициализация счета.
        
        Args:
            account_number: Номер счета
            owner_name: Имя владельца
            initial_balance: Начальный баланс
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        self.is_active = True
        
    def withdraw(self, amount):
        """Снять средства со счета."""
        if not self.is_active:
            raise PaymentProcessingError("Счет не активен")
        if self.balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств на счете")
        self.balance -= amount
        
    def deposit(self, amount):
        """Пополнить счет."""
        if not self.is_active:
            raise PaymentProcessingError("Счет не активен")
        self.balance += amount
        
    def add_transaction(self, transaction):
        """Добавить транзакцию в историю."""
        self.transactions.append(transaction)
        
    def get_balance(self):
        """Получить баланс счета."""
        return self.balance
        
    def get_transaction_history(self):
        """Получить историю транзакций."""
        return self.transactions
        
    def close_account(self):
        """Закрыть счет."""
        self.is_active = False

