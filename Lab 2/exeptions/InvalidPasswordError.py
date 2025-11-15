class InvalidPasswordError(MuseumException):
    """Исключение при неверном пароле."""
    
    def __init__(self, message="Неверный пароль"):
        super().__init__(message)
