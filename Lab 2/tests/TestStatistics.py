class TestStatistics(unittest.TestCase):
    """Тесты для класса Statistics."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.stats = Statistics()
    
    def test_set_metric(self):
        """Тест установки метрики."""
        self.stats.set_metric("daily_visitors", 150)
        metric = self.stats.get_metric("daily_visitors")
        self.assertEqual(metric['value'], 150)
    
    def test_calculate_average(self):
        """Тест расчета среднего."""
        values = [10, 20, 30, 40, 50]
        avg = self.stats.calculate_average(values)
        self.assertEqual(avg, 30)
    
    def test_calculate_growth_rate(self):
        """Тест расчета темпа роста."""
        rate = self.stats.calculate_growth_rate(100, 150)
        self.assertEqual(rate, 50.0)

