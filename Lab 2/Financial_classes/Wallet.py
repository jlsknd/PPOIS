

class Wallet:
    """Класс электронного кошелька."""
    
    def __init__(self, owner, currency="RUB"):
        """
        Инициализация кошелька.
        
        Args:
            owner: Владелец кошелька
            currency: Валюта
        """
        self.owner = owner
        self.currency = currency
        self.balance = 0.0
        self.cards = []
        
    def add_card(self, card):
        """Добавить карту в кошелек."""
        self.cards.append(card)
        
    def remove_card(self, card):
        """Удалить карту из кошелька."""
        if card in self.cards:
            self.cards.remove(card)
            
    def top_up(self, amount):
        """Пополнить кошелек."""
        self.balance += amount
        
    def spend(self, amount):
        """Потратить из кошелька."""
        if self.balance < amount:
            raise InsufficientFundsError("Недостаточно средств в кошельке")
        self.balance -= amount
        
    def get_balance(self):
        """Получить баланс кошелька."""
        return self.balance
