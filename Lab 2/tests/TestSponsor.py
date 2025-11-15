class TestSponsor(unittest.TestCase):
    """Тесты для класса Sponsor."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.sponsor = Sponsor("Tech Corp", 100000.0)
    
    def test_sponsor_exhibit(self):
        """Тест спонсирования выставки."""
        exhibit = Exhibit("Tech Art", "Digital art", "Modern")
        self.sponsor.sponsor_exhibit(exhibit)
        self.assertIn(exhibit, self.sponsor.sponsored_exhibits)
    
    def test_increase_contribution(self):
        """Тест увеличения взноса."""
        self.sponsor.increase_contribution(50000.0)
        self.assertEqual(self.sponsor.contribution_amount, 150000.0)
    
    def test_get_total_contribution(self):
        """Тест получения общего взноса."""
        total = self.sponsor.get_total_contribution()
        self.assertEqual(total, 100000.0)
