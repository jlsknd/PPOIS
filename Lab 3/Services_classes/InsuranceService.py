class InsuranceService:
    """Класс страховых услуг."""
    
    def __init__(self, coverage_rate=0.02):
        """
        Инициализация страховых услуг.
        
        Args:
            coverage_rate: Ставка покрытия (2% от стоимости)
        """
        self.coverage_rate = coverage_rate
        self.policies = []
        
    def create_policy(self, shipment, declared_value):
        """Создать страховой полис."""
        policy = {
            'shipment': shipment,
            'declared_value': declared_value,
            'premium': declared_value * self.coverage_rate,
            'issued_at': datetime.now(),
            'is_active': True
        }
        self.policies.append(policy)
        return policy
        
    def file_claim(self, policy, claim_amount):
        """Подать страховую претензию."""
        if claim_amount <= policy['declared_value']:
            return {
                'approved': True,
                'payout': claim_amount,
                'processed_at': datetime.now()
            }
        return {'approved': False}

