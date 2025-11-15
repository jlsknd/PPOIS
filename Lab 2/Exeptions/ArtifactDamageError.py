class ArtifactDamageError(MuseumException):
    """Исключение при повреждении артефакта."""
    
    def __init__(self, message="Артефакт поврежден"):
        super().__init__(message)
