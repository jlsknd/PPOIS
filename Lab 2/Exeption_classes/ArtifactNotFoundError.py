class ArtifactNotFoundError(MuseumException):
    """Исключение когда артефакт не найден."""
    
    def __init__(self, message="Артефакт не найден"):
        super().__init__(message)
        self.artifact_id = None
