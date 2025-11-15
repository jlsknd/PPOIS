class Dashboard:
    """Класс панели управления."""
    
    def __init__(self):
        """Инициализация панели."""
        self.widgets = {}
        
    def add_widget(self, name, widget_type, data_source):
        """Добавить виджет."""
        self.widgets[name] = {
            'type': widget_type,
            'data_source': data_source,
            'last_updated': datetime.now()
        }
        
    def update_widget(self, name, new_data):
        """Обновить виджет."""
        if name in self.widgets:
            self.widgets[name]['data'] = new_data
            self.widgets[name]['last_updated'] = datetime.now()
            
    def get_widget_data(self, name):
        """Получить данные виджета."""
        return self.widgets.get(name, {}).get('data')
