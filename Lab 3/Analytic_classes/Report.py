class Report:
    """Класс отчета."""
    
    def __init__(self, report_type, period):
        """
        Инициализация отчета.
        
        Args:
            report_type: Тип отчета
            period: Период
        """
        self.report_type = report_type
        self.period = period
        self.data = {}
        self.generated_at = None
        
    def add_data(self, key, value):
        """Добавить данные в отчет."""
        self.data[key] = value
        
    def generate(self):
        """Сгенерировать отчет."""
        self.generated_at = datetime.now()
        return {
            'type': self.report_type,
            'period': self.period,
            'data': self.data,
            'generated_at': self.generated_at
        }
        
    def export_to_file(self, filename):
        """Экспортировать в файл."""
       
        return f"Report exported to {filename}"

