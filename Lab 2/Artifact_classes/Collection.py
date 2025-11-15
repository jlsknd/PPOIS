class Collection:
    """Класс коллекции артефактов."""
    
    def __init__(self, name, curator):
        """
        Инициализация коллекции.
        
        Args:
            name: Название коллекции
            curator: Куратор
        """
        self.name = name
        self.curator = curator
        self.items = []
        self.total_value = 0.0
        
    def add_item(self, artifact):
        """Добавить артефакт в коллекцию."""
        self.items.append(artifact)
        self.total_value += artifact.value
        
    def remove_item(self, artifact):
        """Удалить артефакт из коллекции."""
        if artifact in self.items:
            self.items.remove(artifact)
            self.total_value -= artifact.value
            
    def find_artifact(self, name):
        """Найти артефакт по имени."""
        for item in self.items:
            if item.name == name:
                return item
        raise ArtifactNotFoundError(f"Артефакт {name} не найден")
        
    def get_total_value(self):
        """Получить общую стоимость коллекции."""
        return self.total_value
        
    def catalog_items(self):
        """Каталогизировать артефакты."""
        return [item.inspect() for item in self.items]
