class InsufficientCapacityError(LogisticsException):
    """Исключение при недостаточной вместимости."""
    
    def __init__(self, message="Недостаточная вместимость"):
        super().__init__(message)
