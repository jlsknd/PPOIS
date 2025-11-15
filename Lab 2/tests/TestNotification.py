class TestNotification(unittest.TestCase):
    """Тесты для класса Notification."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.notification = Notification("user@test.com", "Test message", "email")
    
    def test_send(self):
        """Тест отправки уведомления."""
        self.assertTrue(self.notification.send())
        self.assertIsNotNone(self.notification.sent_date)
    
    def test_mark_as_read(self):
        """Тест отметки как прочитанного."""
        self.notification.mark_as_read()
        self.assertTrue(self.notification.is_read)
    
    def test_get_status(self):
        """Тест получения статуса."""
        status = self.notification.get_status()
        self.assertEqual(status, "не прочитано")
        
        self.notification.mark_as_read()
        status = self.notification.get_status()
        self.assertEqual(status, "прочитано")

