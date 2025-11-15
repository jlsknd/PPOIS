class TestAnalytics(unittest.TestCase):
    """Тесты для класса Analytics."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.analytics = Analytics()
    
    def test_record_visitor(self):
        """Тест записи данных посетителя."""
        visitor = Visitor("Test", 30, "test@test.com")
        self.analytics.record_visitor(visitor, datetime.now())
        self.assertEqual(len(self.analytics.visitor_data), 1)
    
    def test_record_revenue(self):
        """Тест записи дохода."""
        self.analytics.record_revenue(500.0, "tickets")
        self.assertEqual(len(self.analytics.revenue_data), 1)
    
    def test_calculate_total_revenue(self):
        """Тест расчета общего дохода."""
        self.analytics.record_revenue(500.0, "tickets")
        self.analytics.record_revenue(300.0, "shop")
        
        total = self.analytics.calculate_total_revenue()
        self.assertEqual(total, 800.0)
    
    def test_get_visitor_count(self):
        """Тест получения количества посетителей."""
        visitor = Visitor("Test", 30, "test@test.com")
        now = datetime.now()
        
        self.analytics.record_visitor(visitor, now)
        count = self.analytics.get_visitor_count(
            datetime(2020, 1, 1),
            datetime(2030, 12, 31)
        )
        self.assertEqual(count, 1)
