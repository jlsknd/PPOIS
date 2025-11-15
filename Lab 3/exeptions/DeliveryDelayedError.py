class DeliveryDelayedError(LogisticsException):
    """Исключение при задержке доставки."""
    
    def __init__(self, message="Доставка задержана"):
        super().__init__(message)

