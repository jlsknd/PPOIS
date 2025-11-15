class Donation:
    """Класс пожертвования."""
    
    def __init__(self, donor_name, amount, purpose):
        """
        Инициализация пожертвования.
        
        Args:
            donor_name: Имя дарителя
            amount: Сумма
            purpose: Цель
        """
        self.donor_name = donor_name
        self.amount = amount
        self.purpose = purpose
        self.donation_date = datetime.now()
        self.is_acknowledged = False
        
    def acknowledge(self):
        """Подтвердить получение."""
        self.is_acknowledged = True
        
    def get_amount(self):
        """Получить сумму."""
        return self.amount
