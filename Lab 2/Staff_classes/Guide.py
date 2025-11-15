class Guide:
    """Класс гида музея."""
    
    def __init__(self, name, languages):
        """
        Инициализация гида.
        
        Args:
            name: Имя гида
            languages: Языки
        """
        self.name = name
        self.languages = languages
        self.tours_conducted = 0
        self.rating = 5.0
        
    def conduct_tour(self, group):
        """Провести экскурсию."""
        self.tours_conducted += 1
        return f"Экскурсия для группы {group.group_name}"
        
    def add_language(self, language):
        """Добавить язык."""
        if language not in self.languages:
            self.languages.append(language)
            
    def update_rating(self, new_rating):
        """Обновить рейтинг."""
        self.rating = (self.rating + new_rating) / 2
        
    def get_rating(self):
        """Получить рейтинг."""
        return self.rating
