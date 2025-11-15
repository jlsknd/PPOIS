class InsufficientFundsError(LogisticsException):
    """Исключение при недостаточных средствах на счету."""
    
    def __init__(self, message="Недостаточно средств"):
        super().__init__(message)

