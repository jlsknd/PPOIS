class UnauthorizedAccessError(LogisticsException):
    """Исключение при попытке неавторизованного доступа."""
    
    def __init__(self, message="Неавторизованный доступ"):
        super().__init__(message)
