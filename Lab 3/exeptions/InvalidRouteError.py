class InvalidRouteError(LogisticsException):
    """Исключение при некорректном маршруте."""
    
    def __init__(self, message="Некорректный маршрут"):
        super().__init__(message)
