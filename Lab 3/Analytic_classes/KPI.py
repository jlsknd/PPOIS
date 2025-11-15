class KPI:
    """Класс ключевых показателей эффективности."""
    
    def __init__(self):
        """Инициализация KPI."""
        self.kpis = {}
        
    def set_kpi(self, name, target, current):
        """Установить KPI."""
        self.kpis[name] = {
            'target': target,
            'current': current,
            'achievement': (current / target * 100) if target > 0 else 0,
            'updated_at': datetime.now()
        }
        
    def get_kpi(self, name):
        """Получить KPI."""
        return self.kpis.get(name)
        
    def get_all_kpis(self):
        """Получить все KPI."""
        return self.kpis
