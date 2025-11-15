class ExhibitClosedError(MuseumException):
    """Исключение когда выставка закрыта."""
    
    def __init__(self, message="Выставка закрыта"):
        super().__init__(message)
