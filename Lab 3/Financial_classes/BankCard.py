class BankCard:
    """Класс банковской карты."""
    
    def __init__(self, card_number, holder_name, cvv, balance):
        """
        Инициализация карты.
        
        Args:
            card_number: Номер карты
            holder_name: Имя держателя
            cvv: CVV код
            balance: Баланс
        """
        self.card_number = card_number
        self.holder_name = holder_name
        self.cvv = cvv
        self.balance = balance
        self.is_blocked = False
        self.expiry_date = None
        self.card_type = "debit"
        
    def withdraw(self, amount):
        """Снять деньги с карты."""
        if self.is_blocked:
            raise PaymentProcessingError("Карта заблокирована")
        if self.balance < amount:
            raise InsufficientFundsError("Недостаточно средств на карте")
        self.balance -= amount
        
    def deposit(self, amount):
        """Пополнить карту."""
        self.balance += amount
        
    def block_card(self):
        """Заблокировать карту."""
        self.is_blocked = True
        
    def verify_cvv(self, cvv):
        """Проверить CVV."""
        return self.cvv == cvv
        
    def get_balance(self):
        """Получить баланс."""
        return self.balance
