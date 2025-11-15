"""
Юнит-тесты для модуля аналитики.
"""

import unittest
from datetime import datetime
from logisticsApp.logistics.analytics import (Analytics, PerformanceMetrics, Report, 
                                 CustomerFeedback, Survey, Dashboard, KPI, Notification)


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


class TestReport(unittest.TestCase):
    """Тесты для класса Report."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.report = Report("monthly", "2024-01")
    
    def test_add_data(self):
        """Тест добавления данных."""
        self.report.add_data("revenue", 50000)
        self.assertIn("revenue", self.report.data)
        
    def test_generate(self):
        """Тест генерации отчета."""
        self.report.add_data("revenue", 50000)
        result = self.report.generate()
        self.assertEqual(result['type'], "monthly")
        self.assertIsNotNone(result['generated_at'])
        
    def test_export_to_file(self):
        """Тест экспорта в файл."""
        result = self.report.export_to_file("report.txt")
        self.assertIn("exported", result.lower())


class TestCustomerFeedback(unittest.TestCase):
    """Тесты для класса CustomerFeedback."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.feedback = CustomerFeedback("Customer1", 5, "Great service")
    
    def test_mark_processed(self):
        """Тест отметки об обработке."""
        self.feedback.mark_processed()
        self.assertTrue(self.feedback.is_processed)
        
    def test_get_rating(self):
        """Тест получения оценки."""
        self.assertEqual(self.feedback.get_rating(), 5)


class TestSurvey(unittest.TestCase):
    """Тесты для класса Survey."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.survey = Survey("Customer Satisfaction", ["Q1", "Q2"])
    
    def test_submit_response(self):
        """Тест отправки ответа."""
        self.survey.submit_response("Customer1", ["A1", "A2"])
        self.assertEqual(len(self.survey.responses), 1)
        
    def test_get_response_count(self):
        """Тест получения количества ответов."""
        self.survey.submit_response("Customer1", ["A1", "A2"])
        self.survey.submit_response("Customer2", ["A1", "A2"])
        self.assertEqual(self.survey.get_response_count(), 2)


class TestDashboard(unittest.TestCase):
    """Тесты для класса Dashboard."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.dashboard = Dashboard()
    
    def test_add_widget(self):
        """Тест добавления виджета."""
        self.dashboard.add_widget("revenue_chart", "chart", "revenue_data")
        self.assertIn("revenue_chart", self.dashboard.widgets)
        
    def test_update_widget(self):
        """Тест обновления виджета."""
        self.dashboard.add_widget("revenue_chart", "chart", "revenue_data")
        self.dashboard.update_widget("revenue_chart", {"value": 1000})
        self.assertEqual(self.dashboard.widgets["revenue_chart"]['data'], {"value": 1000})
        
    def test_get_widget_data(self):
        """Тест получения данных виджета."""
        self.dashboard.add_widget("revenue_chart", "chart", "revenue_data")
        self.dashboard.update_widget("revenue_chart", {"value": 1000})
        data = self.dashboard.get_widget_data("revenue_chart")
        self.assertEqual(data, {"value": 1000})


class TestKPI(unittest.TestCase):
    """Тесты для класса KPI."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.kpi = KPI()
    
    def test_set_kpi(self):
        """Тест установки KPI."""
        self.kpi.set_kpi("deliveries", 100, 80)
        self.assertEqual(self.kpi.get_kpi("deliveries")['achievement'], 80)
        
    def test_get_kpi(self):
        """Тест получения KPI."""
        self.kpi.set_kpi("deliveries", 100, 80)
        result = self.kpi.get_kpi("deliveries")
        self.assertEqual(result['target'], 100)
        self.assertEqual(result['current'], 80)
        
    def test_get_all_kpis(self):
        """Тест получения всех KPI."""
        self.kpi.set_kpi("deliveries", 100, 80)
        self.kpi.set_kpi("revenue", 50000, 45000)
        all_kpis = self.kpi.get_all_kpis()
        self.assertEqual(len(all_kpis), 2)


class TestNotification(unittest.TestCase):
    """Тесты для класса Notification."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.notification = Notification("user@example.com", "Test message", "email")
    
    def test_send(self):
        """Тест отправки уведомления."""
        self.notification.send()
        self.assertIsNotNone(self.notification.sent_at)
        
    def test_mark_as_read(self):
        """Тест отметки как прочитанное."""
        self.notification.mark_as_read()
        self.assertTrue(self.notification.is_read)
        
    def test_get_status(self):
        """Тест получения статуса."""
        self.assertEqual(self.notification.get_status(), "pending")
        self.notification.send()
        self.assertEqual(self.notification.get_status(), "sent")
        self.notification.mark_as_read()
        self.assertEqual(self.notification.get_status(), "read")
