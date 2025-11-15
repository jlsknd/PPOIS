class InvalidDateError(MuseumException):
    """Исключение при некорректной дате."""
    
    def __init__(self, message="Некорректная дата"):
        super().__init__(message)
        self.invalid_date = None
