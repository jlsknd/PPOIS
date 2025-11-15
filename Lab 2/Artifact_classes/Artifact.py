class Artifact:
    """Класс артефакта музея."""
    
    def __init__(self, name, origin, era, value):
        """
        Инициализация артефакта.
        
        Args:
            name: Название артефакта
            origin: Происхождение
            era: Эпоха
            value: Стоимость
        """
        self.name = name
        self.origin = origin
        self.era = era
        self.value = value
        self.condition = "excellent"
        self.location = None
        self.insurance_value = value * 1.5
        
    def inspect(self):
        """Осмотреть артефакт."""
        return {
            'name': self.name,
            'condition': self.condition,
            'location': self.location
        }
        
    def repair(self):
        """Отреставрировать артефакт."""
        if self.condition == "damaged":
            self.condition = "good"
            return True
        return False
        
    def damage(self, damage_level):
        """Повредить артефакт."""
        if damage_level > 50:
            self.condition = "damaged"
            raise ArtifactDamageError(f"Артефакт {self.name} поврежден")
        elif damage_level > 20:
            self.condition = "fair"
            
    def set_location(self, location):
        """Установить местоположение артефакта."""
        self.location = location
        
    def get_value(self):
        """Получить стоимость артефакта."""
        return self.value
        
    def update_insurance_value(self, new_value):
        """Обновить страховую стоимость."""
        self.insurance_value = new_value

