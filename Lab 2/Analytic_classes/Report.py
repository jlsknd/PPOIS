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
        self.generated_date = None
        
    def add_data(self, key, value):
        """Добавить данные."""
        self.data[key] = value
        
    def generate(self):
        """Сгенерировать отчет."""
        self.generated_date = datetime.now()
        return {
            'type': self.report_type,
            'period': self.period,
            'data': self.data,
            'generated': self.generated_date
        }
        
    def export_to_file(self, filename):
        """Экспортировать в файл."""
        return f"Отчет экспортирован в {filename}"
