class Exhibit:
    """Класс выставки."""
    
    def __init__(self, title, description, category):
        """
        Инициализация выставки.
        
        Args:
            title: Название выставки
            description: Описание
            category: Категория
        """
        self.title = title
        self.description = description
        self.category = category
        self.artifacts = []
        self.is_open = False
        self.visitor_count = 0
        self.rating = 0.0
        
    def add_artifact(self, artifact):
        """Добавить артефакт на выставку."""
        self.artifacts.append(artifact)
        artifact.set_location(self.title)
        
    def remove_artifact(self, artifact):
        """Удалить артефакт с выставки."""
        if artifact in self.artifacts:
            self.artifacts.remove(artifact)
            artifact.set_location(None)
            
    def open_exhibit(self):
        """Открыть выставку."""
        self.is_open = True
        
    def close_exhibit(self):
        """Закрыть выставку."""
        self.is_open = False
        
    def record_visitor(self):
        """Зарегистрировать посетителя."""
        self.visitor_count += 1
        
    def rate_exhibit(self, rating):
        """Оценить выставку."""
        self.rating = (self.rating + rating) / 2
        
    def get_artifacts(self):
        """Получить список артефактов."""
        return self.artifacts
