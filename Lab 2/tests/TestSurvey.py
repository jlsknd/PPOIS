class TestSurvey(unittest.TestCase):
    """Тесты для класса Survey."""
    
    def setUp(self):
        """Подготовка к тестам."""
        questions = ["Question 1", "Question 2"]
        self.survey = Survey("Visitor Survey", questions)
    
    def test_submit_response(self):
        """Тест отправки ответа."""
        self.survey.submit_response({"q1": "answer1"})
        self.assertEqual(len(self.survey.responses), 1)
    
    def test_get_response_count(self):
        """Тест получения количества ответов."""
        self.survey.submit_response({"q1": "answer1"})
        self.survey.submit_response({"q1": "answer2"})
        
        count = self.survey.get_response_count()
        self.assertEqual(count, 2)
