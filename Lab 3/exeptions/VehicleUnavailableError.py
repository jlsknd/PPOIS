class VehicleUnavailableError(LogisticsException):
    """Исключение когда транспорт недоступен."""
    
    def __init__(self, message="Транспорт недоступен"):
        super().__init__(message)
