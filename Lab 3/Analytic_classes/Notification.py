class Notification:
    """Класс уведомления."""
    
    def __init__(self, recipient, message, notification_type):
        """
        Инициализация уведомления.
        
        Args:
            recipient: Получатель
            message: Сообщение
            notification_type: Тип (email, sms, push)
        """
        self.recipient = recipient
        self.message = message
        self.notification_type = notification_type
        self.sent_at = None
        self.is_read = False
        
    def send(self):
        """Отправить уведомление."""
        self.sent_at = datetime.now()
        
    def mark_as_read(self):
        """Отметить как прочитанное."""
        self.is_read = True
        
    def get_status(self):
        """Получить статус."""
        if self.is_read:
            return "read"
        elif self.sent_at:
            return "sent"
        return "pending"
