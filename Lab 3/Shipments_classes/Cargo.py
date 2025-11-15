class Cargo:
    """Класс груза/посылки (отдельный предмет в отправке)."""
    
    def __init__(self, cargo_id, description, weight_kg, dimensions):
        """
        Инициализация груза.
        
        Args:
            cargo_id: ID груза
            description: Описание груза
            weight_kg: Вес в кг
            dimensions: Размеры (dict с ключами length, width, height в см)
        """
        self.cargo_id = cargo_id
        self.description = description
        self.weight_kg = weight_kg
        self.dimensions = dimensions  # {'length': x, 'width': y, 'height': z}
        self.is_fragile = False
        self.is_hazardous = False
        self.temperature_controlled = False
        self.barcode = None
        self.packaging_type = "standard"
        self.handling_instructions = None
        
    def mark_fragile(self):
        """Отметить как хрупкий груз."""
        self.is_fragile = True
        
    def mark_hazardous(self):
        """Отметить как опасный груз."""
        self.is_hazardous = True
        
    def set_temperature_control(self, required=True):
        """Установить требование контроля температуры."""
        self.temperature_controlled = required
        
    def assign_barcode(self, barcode):
        """Присвоить штрих-код."""
        self.barcode = barcode
        
    def calculate_volume(self):
        """Рассчитать объем груза в кубометрах."""
        if self.dimensions:
            length = self.dimensions.get('length', 0)
            width = self.dimensions.get('width', 0)
            height = self.dimensions.get('height', 0)
            # Переводим из см³ в м³
            return (length * width * height) / 1000000
        return 0
