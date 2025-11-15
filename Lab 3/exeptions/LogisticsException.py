class LogisticsException(Exception):
    """Базовое исключение для системы управления логистикой."""
    
    def __init__(self, message="Ошибка системы управления логистикой"):
        super().__init__(message)
        self.message = message
