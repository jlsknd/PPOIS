class TestDonation(unittest.TestCase):
    """Тесты для класса Donation."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.donation = Donation("John Doe", 5000.0, "Artifact restoration")
    
    def test_acknowledge(self):
        """Тест подтверждения получения."""
        self.donation.acknowledge()
        self.assertTrue(self.donation.is_acknowledged)
    
    def test_get_amount(self):
        """Тест получения суммы."""
        self.assertEqual(self.donation.get_amount(), 5000.0)
