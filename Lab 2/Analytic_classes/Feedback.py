class Feedback:
    """Класс обратной связи."""
    
    def __init__(self, visitor, rating, comment):
        """
        Инициализация обратной связи.
        
        Args:
            visitor: Посетитель
            rating: Оценка
            comment: Комментарий
        """
        self.visitor = visitor
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.now()
        self.is_processed = False
        
    def mark_processed(self):
        """Отметить как обработанное."""
        self.is_processed = True
        
    def get_rating(self):
        """Получить оценку."""
        return self.rating
