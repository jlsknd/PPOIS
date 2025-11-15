class InsufficientFundsError(MuseumException):
    """Исключение при недостаточных средствах на счету."""
    
    def __init__(self, message="Недостаточно средств"):
        super().__init__(message)
        self.amount_required = None

