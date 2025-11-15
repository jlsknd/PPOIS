class InvalidDateError(LogisticsException):
    """Исключение при некорректной дате."""
    
    def __init__(self, message="Некорректная дата"):
        super().__init__(message)
