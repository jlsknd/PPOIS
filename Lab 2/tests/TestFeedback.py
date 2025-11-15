class TestFeedback(unittest.TestCase):
    """Тесты для класса Feedback."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.visitor = Visitor("Reviewer", 35, "review@test.com")
        self.feedback = Feedback(self.visitor, 5, "Great experience!")
    
    def test_mark_processed(self):
        """Тест отметки как обработанного."""
        self.feedback.mark_processed()
        self.assertTrue(self.feedback.is_processed)
    
    def test_get_rating(self):
        """Тест получения оценки."""
        self.assertEqual(self.feedback.get_rating(), 5)
