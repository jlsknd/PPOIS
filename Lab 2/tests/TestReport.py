class TestReport(unittest.TestCase):
    """Тесты для класса Report."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.report = Report("monthly", "January 2024")
    
    def test_add_data(self):
        """Тест добавления данных."""
        self.report.add_data("visitors", 1000)
        self.assertEqual(self.report.data["visitors"], 1000)
    
    def test_generate(self):
        """Тест генерации отчета."""
        self.report.add_data("visitors", 1000)
        result = self.report.generate()
        
        self.assertEqual(result['type'], "monthly")
        self.assertIsNotNone(result['generated'])
    
    def test_export_to_file(self):
        """Тест экспорта в файл."""
        result = self.report.export_to_file("report.pdf")
        self.assertIn("report.pdf", result)
