class ShipmentNotFoundError(LogisticsException):
    """Исключение когда груз не найден."""
    
    def __init__(self, message="Груз не найден"):
        super().__init__(message)
