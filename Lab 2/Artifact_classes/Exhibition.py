class Exhibition:
    """Класс большой выставки."""
    
    def __init__(self, name, start_date, end_date):
        """
        Инициализация выставки.
        
        Args:
            name: Название
            start_date: Дата начала
            end_date: Дата окончания
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.exhibits = []
        self.sponsors = []
        
    def add_exhibit(self, exhibit):
        """Добавить экспозицию."""
        self.exhibits.append(exhibit)
        
    def add_sponsor(self, sponsor):
        """Добавить спонсора."""
        self.sponsors.append(sponsor)
        
    def is_active(self):
        """Проверить активность выставки."""
        now = datetime.now()
        return self.start_date <= now <= self.end_date
        
    def get_exhibits(self):
        """Получить список экспозиций."""
        return self.exhibits
