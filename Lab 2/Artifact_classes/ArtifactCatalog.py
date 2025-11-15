class ArtifactCatalog:
    """Класс каталога артефактов."""
    
    def __init__(self):
        """Инициализация каталога."""
        self.artifacts = {}
        self.categories = {}
        
    def register_artifact(self, artifact_id, artifact):
        """Зарегистрировать артефакт."""
        self.artifacts[artifact_id] = artifact
        
    def search_by_era(self, era):
        """Поиск по эпохе."""
        return [a for a in self.artifacts.values() if a.era == era]
        
    def search_by_origin(self, origin):
        """Поиск по происхождению."""
        return [a for a in self.artifacts.values() if a.origin == origin]
        
    def get_artifact(self, artifact_id):
        """Получить артефакт по ID."""
        if artifact_id not in self.artifacts:
            raise ArtifactNotFoundError(f"Артефакт с ID {artifact_id} не найден")
        return self.artifacts[artifact_id]
        
    def categorize(self, category, artifacts):
        """Категоризировать артефакты."""
        self.categories[category] = artifacts
