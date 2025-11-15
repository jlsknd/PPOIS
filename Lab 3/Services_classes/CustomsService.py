class CustomsService:
    """Класс таможенного оформления."""
    
    def __init__(self):
        """Инициализация таможенной службы."""
        self.declarations = []
        self.processing_fee = 100.0
        
    def file_declaration(self, shipment, customs_value):
        """Подать таможенную декларацию."""
        declaration = {
            'shipment': shipment,
            'customs_value': customs_value,
            'status': 'pending',
            'filed_at': datetime.now()
        }
        self.declarations.append(declaration)
        return declaration
        
    def approve_declaration(self, declaration):
        """Одобрить декларацию."""
        declaration['status'] = 'approved'
        declaration['approved_at'] = datetime.now()
        
    def calculate_duties(self, customs_value, duty_rate=0.1):
        """Рассчитать таможенные пошлины."""
        return customs_value * duty_rate + self.processing_fee
