class TestAnalytics(unittest.TestCase):
    """Тесты для класса Analytics."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.analytics = Analytics()
    
    def test_record_revenue(self):
        """Тест записи выручки."""
        self.analytics.record_revenue(1000, "freight")
        self.assertEqual(len(self.analytics.revenue_records), 1)
        
    def test_record_delivery(self):
        """Тест записи доставки."""
        self.analytics.record_delivery("DEL001", True)
        self.assertEqual(len(self.analytics.delivery_records), 1)
        
    def test_calculate_total_revenue(self):
        """Тест расчета общей выручки."""
        self.analytics.record_revenue(1000, "freight")
        self.analytics.record_revenue(500, "storage")
        total = self.analytics.calculate_total_revenue()
        self.assertEqual(total, 1500)
        
    def test_get_delivery_success_rate(self):
        """Тест процента успешных доставок."""
        self.analytics.record_delivery("DEL001", True)
        self.analytics.record_delivery("DEL002", True)
        self.analytics.record_delivery("DEL003", False)
        rate = self.analytics.get_delivery_success_rate()
        self.assertAlmostEqual(rate, 66.67, places=1)

