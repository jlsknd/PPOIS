class Analytics:
    """Класс аналитики музея."""
    
    def __init__(self):
        """Инициализация аналитики."""
        self.visitor_data = []
        self.revenue_data = []
        self.exhibit_ratings = defaultdict(list)
        
    def record_visitor(self, visitor, visit_date):
        """Записать данные посетителя."""
        self.visitor_data.append({
            'visitor': visitor,
            'date': visit_date
        })
        
    def record_revenue(self, amount, source):
        """Записать доход."""
        self.revenue_data.append({
            'amount': amount,
            'source': source,
            'date': datetime.now()
        })
        
    def calculate_total_revenue(self):
        """Рассчитать общий доход."""
        return sum(r['amount'] for r in self.revenue_data)
        
    def get_visitor_count(self, start_date, end_date):
        """Получить количество посетителей за период."""
        count = 0
        for data in self.visitor_data:
            if start_date <= data['date'] <= end_date:
                count += 1
        return count
        
    def analyze_popular_exhibits(self):
        """Анализировать популярные выставки."""
        return sorted(self.exhibit_ratings.items(), 
                     key=lambda x: sum(x[1])/len(x[1]) if x[1] else 0, 
                     reverse=True)
