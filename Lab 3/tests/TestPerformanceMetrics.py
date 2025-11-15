class TestPerformanceMetrics(unittest.TestCase):
    """Тесты для класса PerformanceMetrics."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.metrics = PerformanceMetrics()
    
    def test_set_metric(self):
        """Тест установки метрики."""
        self.metrics.set_metric("deliveries", 100)
        self.assertEqual(self.metrics.get_metric("deliveries"), 100)
        
    def test_get_metric(self):
        """Тест получения метрики."""
        self.metrics.set_metric("deliveries", 100)
        value = self.metrics.get_metric("deliveries")
        self.assertEqual(value, 100)
        
    def test_calculate_average_delivery_time(self):
        """Тест расчета среднего времени доставки."""
        avg = self.metrics.calculate_average_delivery_time([10, 20, 30])
        self.assertEqual(avg, 20)
        
    def test_calculate_vehicle_utilization(self):
        """Тест расчета использования транспорта."""
        utilization = self.metrics.calculate_vehicle_utilization(10, 7)
        self.assertEqual(utilization, 70)
