class SecurityViolationError(MuseumException):
    """Исключение при нарушении безопасности."""
    
    def __init__(self, message="Нарушение безопасности"):
        super().__init__(message)
