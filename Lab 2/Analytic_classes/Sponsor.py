class Sponsor:
    """Класс спонсора."""
    
    def __init__(self, name, contribution_amount):
        """
        Инициализация спонсора.
        
        Args:
            name: Название спонсора
            contribution_amount: Сумма взноса
        """
        self.name = name
        self.contribution_amount = contribution_amount
        self.sponsored_exhibits = []
        self.contract_date = datetime.now()
        
    def sponsor_exhibit(self, exhibit):
        """Спонсировать выставку."""
        self.sponsored_exhibits.append(exhibit)
        
    def increase_contribution(self, amount):
        """Увеличить взнос."""
        self.contribution_amount += amount
        
    def get_total_contribution(self):
        """Получить общий взнос."""
        return self.contribution_amount

