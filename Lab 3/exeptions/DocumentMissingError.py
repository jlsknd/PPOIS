class DocumentMissingError(LogisticsException):
    """Исключение при отсутствии документов."""
    
    def __init__(self, message="Отсутствуют необходимые документы"):
        super().__init__(message)
