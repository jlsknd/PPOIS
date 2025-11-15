class CustomerFeedback:
    """Класс обратной связи от клиентов."""
    
    def __init__(self, customer, rating, comment):
        """
        Инициализация обратной связи.
        
        Args:
            customer: Клиент
            rating: Оценка (1-5)
            comment: Комментарий
        """
        self.customer = customer
        self.rating = rating
        self.comment = comment
        self.submitted_at = datetime.now()
        self.is_processed = False
        
    def mark_processed(self):
        """Отметить как обработанное."""
        self.is_processed = True
        
    def get_rating(self):
        """Получить оценку."""
        return self.rating
