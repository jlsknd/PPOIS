class Notification:
    """Класс уведомления."""
    
    def __init__(self, recipient, message, notification_type):
        """
        Инициализация уведомления.
        
        Args:
            recipient: Получатель
            message: Сообщение
            notification_type: Тип уведомления
        """
        self.recipient = recipient
        self.message = message
        self.notification_type = notification_type
        self.sent_date = None
        self.is_read = False
        
    def send(self):
        """Отправить уведомление."""
        self.sent_date = datetime.now()
        return True
        
    def mark_as_read(self):
        """Отметить как прочитанное."""
        self.is_read = True
        
    def get_status(self):
        """Получить статус."""
        return "прочитано" if self.is_read else "не прочитано"
