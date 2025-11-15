class Newsletter:
    """Класс рассылки."""
    
    def __init__(self, subject, content):
        """
        Инициализация рассылки.
        
        Args:
            subject: Тема
            content: Содержание
        """
        self.subject = subject
        self.content = content
        self.subscribers = []
        self.sent_date = None
        
    def add_subscriber(self, email):
        """Добавить подписчика."""
        if email not in self.subscribers:
            self.subscribers.append(email)
            
    def remove_subscriber(self, email):
        """Удалить подписчика."""
        if email in self.subscribers:
            self.subscribers.remove(email)
            
    def send_newsletter(self):
        """Отправить рассылку."""
        self.sent_date = datetime.now()
        return len(self.subscribers)

