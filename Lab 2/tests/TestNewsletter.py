class TestNewsletter(unittest.TestCase):
    """Тесты для класса Newsletter."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.newsletter = Newsletter("Monthly Update", "Content here")
    
    def test_add_subscriber(self):
        """Тест добавления подписчика."""
        self.newsletter.add_subscriber("user1@test.com")
        self.assertIn("user1@test.com", self.newsletter.subscribers)
    
    def test_remove_subscriber(self):
        """Тест удаления подписчика."""
        self.newsletter.add_subscriber("user1@test.com")
        self.newsletter.remove_subscriber("user1@test.com")
        self.assertNotIn("user1@test.com", self.newsletter.subscribers)
    
    def test_send_newsletter(self):
        """Тест отправки рассылки."""
        self.newsletter.add_subscriber("user1@test.com")
        self.newsletter.add_subscriber("user2@test.com")
        
        count = self.newsletter.send_newsletter()
        self.assertEqual(count, 2)
        self.assertIsNotNone(self.newsletter.sent_date)

