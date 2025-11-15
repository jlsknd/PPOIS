class PaymentProcessingError(LogisticsException):
    """Исключение при ошибке обработки платежа."""
    
    def __init__(self, message="Ошибка обработки платежа"):
        super().__init__(message)
