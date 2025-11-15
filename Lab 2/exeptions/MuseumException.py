class MuseumException(Exception):
    """Базовое исключение для системы управления музеем."""
    
    def __init__(self, message="Ошибка системы управления музеем"):
        super().__init__(message)
        self.message = message

