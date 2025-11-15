class PaymentProcessor:
    """Класс обработчика платежей."""
    
    def __init__(self):
        """Инициализация обработчика платежей."""
        self.processed_payments = []
        self.commission_rate = 0.02
        
    def process_payment(self, payment, card):
        """
        Обработать платеж.
        
        Args:
            payment: Объект платежа
            card: Банковская карта
        """
        total_amount = payment.amount * (1 + self.commission_rate)
        card.withdraw(total_amount)
        payment.process()
        payment.complete(f"TXN{len(self.processed_payments)}")
        self.processed_payments.append(payment)
        return True
        
    def refund_payment(self, payment, card):
        """Вернуть платеж."""
        if payment in self.processed_payments:
            card.deposit(payment.amount)
            payment.cancel()
            return True
        return False
        
    def transfer_money(self, from_card, to_card, amount):
        """Перевести деньги с одной карты на другую."""
        from_card.withdraw(amount)
        to_card.deposit(amount)
        return True
        
    def get_commission(self, amount):
        """Рассчитать комиссию."""
        return amount * self.commission_rate
