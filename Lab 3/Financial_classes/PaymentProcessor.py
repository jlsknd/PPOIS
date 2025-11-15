class PaymentProcessor:
    """Класс обработки платежей."""
    
    def __init__(self):
        """Инициализация процессора платежей."""
        self.commission_rate = 0.02
        
    def process_payment(self, payment, card):
        """Обработать платеж."""
        try:
            payment.process()
            card.withdraw(payment.amount)
            payment.complete()
            return True
        except Exception as e:
            payment.cancel()
            raise PaymentProcessingError(f"Ошибка обработки платежа: {str(e)}")
            
    def transfer_money(self, from_card, to_card, amount):
        """Перевести деньги между картами."""
        from_card.withdraw(amount)
        to_card.deposit(amount)
        
    def get_commission(self, amount):
        """Получить комиссию."""
        return amount * self.commission_rate
