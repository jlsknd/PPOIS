class SecurityGuard:
    """Класс охранника."""
    
    def __init__(self, name, shift):
        """
        Инициализация охранника.
        
        Args:
            name: Имя охранника
            shift: Смена
        """
        self.name = name
        self.shift = shift
        self.assigned_area = None
        self.incidents_reported = []
        
    def patrol_area(self, area):
        """Патрулировать зону."""
        return f"Патрулирование зоны {area}"
        
    def report_incident(self, incident):
        """Сообщить об инциденте."""
        self.incidents_reported.append({
            'incident': incident,
            'timestamp': datetime.now()
        })
        
    def assign_area(self, area):
        """Назначить зону."""
        self.assigned_area = area
        
    def get_incidents_count(self):
        """Получить количество инцидентов."""
        return len(self.incidents_reported)
