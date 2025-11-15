class CapacityExceededError(MuseumException):
    """Исключение когда превышена вместимость."""
    
    def __init__(self, message="Превышена вместимость"):
        super().__init__(message)
