class Analytics:
    """Класс аналитики."""
    
    def __init__(self):
        """Инициализация аналитики."""
        self.revenue_records = []
        self.delivery_records = []
        
    def record_revenue(self, amount, source):
        """Записать выручку."""
        self.revenue_records.append({
            'amount': amount,
            'source': source,
            'timestamp': datetime.now()
        })
        
    def record_delivery(self, delivery_id, success):
        """Записать доставку."""
        self.delivery_records.append({
            'delivery_id': delivery_id,
            'success': success,
            'timestamp': datetime.now()
        })
        
    def calculate_total_revenue(self):
        """Рассчитать общую выручку."""
        return sum(r['amount'] for r in self.revenue_records)
        
    def get_delivery_success_rate(self):
        """Получить процент успешных доставок."""
        if not self.delivery_records:
            return 0
        successful = sum(1 for d in self.delivery_records if d['success'])
        return (successful / len(self.delivery_records)) * 100

