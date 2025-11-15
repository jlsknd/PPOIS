class OverweightError(LogisticsException):
    """Исключение при превышении веса."""
    
    def __init__(self, message="Превышен допустимый вес"):
        super().__init__(message)
