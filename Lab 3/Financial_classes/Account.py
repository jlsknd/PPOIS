class Account:
    """Класс счета."""
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        """
        Инициализация счета.
        
        Args:
            account_number: Номер счета
            account_holder: Владелец счета
            initial_balance: Начальный баланс
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.is_active = True
        self.transactions = []
        self.account_type = "checking"
        
    def deposit(self, amount):
        """Пополнить счет."""
        self.balance += amount
        self.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': datetime.now()
        })
        
    def withdraw(self, amount):
        """Снять со счета."""
        if self.balance < amount:
            raise InsufficientFundsError("Недостаточно средств")
        self.balance -= amount
        self.transactions.append({
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': datetime.now()
        })
        
    def close_account(self):
        """Закрыть счет."""
        self.is_active = False
