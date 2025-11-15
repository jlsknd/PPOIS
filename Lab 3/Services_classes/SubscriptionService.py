class SubscriptionService:
    """Класс услуги подписки."""
    
    def __init__(self, plan_name, monthly_fee, benefits):
        """
        Инициализация услуги подписки.
        
        Args:
            plan_name: Название плана
            monthly_fee: Ежемесячная плата
            benefits: Преимущества
        """
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
        self.benefits = benefits
        self.subscribers = []
        
    def subscribe(self, customer):
        """Подписать клиента."""
        subscription = {
            'customer': customer,
            'start_date': datetime.now(),
            'next_billing_date': datetime.now() + timedelta(days=30),
            'is_active': True
        }
        self.subscribers.append(subscription)
        return subscription
        
    def cancel_subscription(self, customer):
        """Отменить подписку."""
        for sub in self.subscribers:
            if sub['customer'] == customer:
                sub['is_active'] = False
                return True
        return False
        
    def get_active_subscribers_count(self):
        """Получить количество активных подписчиков."""
        return sum(1 for sub in self.subscribers if sub['is_active'])
