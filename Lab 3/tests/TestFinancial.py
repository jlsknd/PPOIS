"""
Юнит-тесты для модуля финансов.
"""

import unittest
from logisticsApp.logistics.financial import BankCard, Payment, Invoice, Transaction, Account, PaymentProcessor, Receipt
from logisticsApp.logistics.exceptions import InsufficientFundsError, PaymentProcessingError


class TestBankCard(unittest.TestCase):
    """Тесты для класса BankCard."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.card = BankCard("1111", "John", "123", 1000)
    
    def test_withdraw(self):
        """Тест снятия денег."""
        self.card.withdraw(500)
        self.assertEqual(self.card.balance, 500)
        
    def test_withdraw_insufficient_funds(self):
        """Тест снятия при недостатке средств."""
        card = BankCard("1111", "John", "123", 100)
        with self.assertRaises(InsufficientFundsError):
            card.withdraw(500)
            
    def test_deposit(self):
        """Тест пополнения."""
        self.card.deposit(500)
        self.assertEqual(self.card.balance, 1500)
        
    def test_block_card(self):
        """Тест блокировки карты."""
        self.card.block_card()
        self.assertTrue(self.card.is_blocked)
        
    def test_verify_cvv(self):
        """Тест проверки CVV."""
        self.assertTrue(self.card.verify_cvv("123"))
        self.assertFalse(self.card.verify_cvv("456"))
        
    def test_get_balance(self):
        """Тест получения баланса."""
        self.assertEqual(self.card.get_balance(), 1000)


class TestPayment(unittest.TestCase):
    """Тесты для класса Payment."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.payment = Payment(100, "card", "Test")
    
    def test_process(self):
        """Тест обработки платежа."""
        self.payment.process()
        self.assertEqual(self.payment.status, "processing")
        
    def test_complete(self):
        """Тест завершения платежа."""
        payment = Payment(100, "card", "Test")
        payment.complete()
        self.assertEqual(payment.status, "completed")
        
    def test_cancel(self):
        """Тест отмены платежа."""
        payment = Payment(100, "card", "Test")
        payment.cancel()
        self.assertEqual(payment.status, "cancelled")


class TestInvoice(unittest.TestCase):
    """Тесты для класса Invoice."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.invoice = Invoice("INV001", "Customer", 1000, ["Service"])
    
    def test_mark_as_paid(self):
        """Тест отметки об оплате."""
        payment = Payment(1000, "card", "Invoice payment")
        self.invoice.mark_as_paid(payment)
        self.assertTrue(self.invoice.is_paid)
        
    def test_add_service(self):
        """Тест добавления услуги."""
        invoice = Invoice("INV001", "Customer", 1000, ["Service1"])
        invoice.add_service("Service2")
        self.assertEqual(len(invoice.services), 2)


class TestTransaction(unittest.TestCase):
    """Тесты для класса Transaction."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.from_acc = Account("ACC001", "John", 1000)
        self.to_acc = Account("ACC002", "Jane", 500)
    
    def test_execute(self):
        """Тест выполнения транзакции."""
        transaction = Transaction(self.from_acc, self.to_acc, 300)
        transaction.execute()
        self.assertEqual(self.from_acc.balance, 700)
        self.assertEqual(self.to_acc.balance, 800)
        self.assertEqual(transaction.status, "completed")
        
    def test_execute_insufficient_funds(self):
        """Тест выполнения без средств."""
        from_acc = Account("ACC001", "John", 100)
        to_acc = Account("ACC002", "Jane", 500)
        transaction = Transaction(from_acc, to_acc, 300)
        with self.assertRaises(InsufficientFundsError):
            transaction.execute()
            
    def test_rollback(self):
        """Тест отката транзакции."""
        from_acc = Account("ACC001", "John", 1000)
        to_acc = Account("ACC002", "Jane", 500)
        transaction = Transaction(from_acc, to_acc, 300)
        transaction.execute()
        transaction.rollback()
        self.assertEqual(from_acc.balance, 1000)
        self.assertEqual(to_acc.balance, 500)


class TestAccount(unittest.TestCase):
    """Тесты для класса Account."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.account = Account("ACC001", "John", 1000)
    
    def test_deposit(self):
        """Тест пополнения счета."""
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)
        
    def test_withdraw(self):
        """Тест снятия со счета."""
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)
        
    def test_withdraw_insufficient(self):
        """Тест снятия без средств."""
        account = Account("ACC001", "John", 100)
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(300)
            
    def test_close_account(self):
        """Тест закрытия счета."""
        self.account.close_account()
        self.assertFalse(self.account.is_active)


class TestPaymentProcessor(unittest.TestCase):
    """Тесты для класса PaymentProcessor."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.processor = PaymentProcessor()
    
    def test_process_payment(self):
        """Тест обработки платежа."""
        card = BankCard("1111", "John", "123", 1000)
        payment = Payment(500, "card", "Test")
        result = self.processor.process_payment(payment, card)
        self.assertTrue(result)
        self.assertEqual(payment.status, "completed")
        
    def test_transfer_money(self):
        """Тест перевода денег."""
        card1 = BankCard("1111", "John", "123", 1000)
        card2 = BankCard("2222", "Jane", "456", 500)
        self.processor.transfer_money(card1, card2, 300)
        self.assertEqual(card1.balance, 700)
        self.assertEqual(card2.balance, 800)
        
    def test_get_commission(self):
        """Тест получения комиссии."""
        commission = self.processor.get_commission(1000)
        self.assertEqual(commission, 20)


class TestReceipt(unittest.TestCase):
    """Тесты для класса Receipt."""
    
    def setUp(self):
        """Подготовка к тестам."""
        payment = Payment(100, "card", "Test")
        self.receipt = Receipt(payment, "Customer")
    
    def test_generate_number(self):
        """Тест генерации номера."""
        self.receipt.generate_number()
        self.assertIsNotNone(self.receipt.receipt_number)
        
    def test_get_total(self):
        """Тест получения суммы."""
        self.assertEqual(self.receipt.get_total(), 100)
