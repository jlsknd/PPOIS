class BankCard:
    """Класс банковской карты для платежей."""
    
    def __init__(self, card_number, holder_name, cvv, balance=0.0):
        """
        Инициализация банковской карты.
        
        Args:
            card_number: Номер карты
            holder_name: Имя держателя
            cvv: CVV код
            balance: Баланс карты
        """
        self.card_number = card_number
        self.holder_name = holder_name
        self.cvv = cvv
        self.balance = balance
        self.is_blocked = False
        
    def withdraw(self, amount):
        """Снять средства с карты."""
        if self.is_blocked:
            raise PaymentProcessingError("Карта заблокирована")
        if self.balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств. Доступно: {self.balance}")
        self.balance -= amount
        return True
        
    def deposit(self, amount):
        """Пополнить карту."""
        if self.is_blocked:
            raise PaymentProcessingError("Карта заблокирована")
        self.balance += amount
        return True
        
    def block_card(self):
        """Заблокировать карту."""
        self.is_blocked = True
        
    def unblock_card(self):
        """Разблокировать карту."""
        self.is_blocked = False
        
    def get_balance(self):
        """Получить баланс карты."""
        return self.balance
        
    def verify_cvv(self, cvv):
        """Проверить CVV код."""
        return self.cvv == cvv
