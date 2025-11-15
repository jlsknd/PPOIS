class Membership:
    """Класс членства в музее."""
    
    def __init__(self, member, membership_type, duration_months):
        """
        Инициализация членства.
        
        Args:
            member: Член
            membership_type: Тип членства
            duration_months: Длительность в месяцах
        """
        self.member = member
        self.membership_type = membership_type
        self.start_date = datetime.now()
        self.end_date = datetime.now() + timedelta(days=30*duration_months)
        self.benefits = []
        self.is_active = True
        
    def is_valid(self):
        """Проверить действительность членства."""
        return self.is_active and datetime.now() <= self.end_date
        
    def renew(self, months):
        """Продлить членство."""
        self.end_date += timedelta(days=30*months)
        self.is_active = True
        
    def cancel(self):
        """Отменить членство."""
        self.is_active = False
        
    def add_benefit(self, benefit):
        """Добавить привилегию."""
        self.benefits.append(benefit)
        
    def get_benefits(self):
        """Получить список привилегий."""
        return self.benefits
