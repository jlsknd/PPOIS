class Workshop:
    """Класс мастер-класса."""
    
    def __init__(self, topic, instructor, fee):
        """
        Инициализация мастер-класса.
        
        Args:
            topic: Тема
            instructor: Инструктор
            fee: Стоимость
        """
        self.topic = topic
        self.instructor = instructor
        self.fee = fee
        self.participants = []
        self.materials = []
        
    def enroll_participant(self, visitor, payment):
        """Записать участника."""
        if payment.amount >= self.fee:
            self.participants.append(visitor)
            return True
        return False
        
    def add_material(self, material):
        """Добавить материал."""
        self.materials.append(material)
        
    def conduct(self):
        """Провести мастер-класс."""
        return f"Мастер-класс по теме {self.topic} проведен"

