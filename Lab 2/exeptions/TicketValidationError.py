class TicketValidationError(MuseumException):
    """Исключение при ошибке валидации билета."""
    
    def __init__(self, message="Ошибка валидации билета"):
        super().__init__(message)
