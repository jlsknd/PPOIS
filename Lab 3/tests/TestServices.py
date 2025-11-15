"""
Юнит-тесты для модуля services-услуги.
"""

import unittest
from datetime import datetime
from logisticsApp.logistics.services import (FreightService, ExpressDelivery, CustomsService, 
                                WarehouseService, PackagingService, InsuranceService,
                                CustomerSupport, SubscriptionService)


class TestFreightService(unittest.TestCase):
    """Тесты для класса FreightService."""
    
    def test_calculate_cost(self):
        """Тест расчета стоимости."""
        service = FreightService("FS001", "domestic", 2.0)
        cost = service.calculate_cost(1000, 500)
        self.assertTrue(cost > 0)
        
    def test_add_shipment(self):
        """Тест добавления груза."""
        service = FreightService("FS001", "domestic", 2.0)
        shipment = {'id': 'SHP001'}
        service.add_shipment(shipment)
        self.assertEqual(len(service.active_shipments), 1)
        
    def test_complete_shipment(self):
        """Тест завершения доставки груза."""
        service = FreightService("FS001", "domestic", 2.0)
        shipment = {'id': 'SHP001'}
        service.add_shipment(shipment)
        service.complete_shipment(shipment)
        self.assertEqual(len(service.active_shipments), 0)


class TestExpressDelivery(unittest.TestCase):
    """Тесты для класса ExpressDelivery."""
    
    def test_calculate_cost(self):
        """Тест расчета стоимости с наценкой."""
        express = ExpressDelivery("EXP001", 24)
        cost = express.calculate_cost(1000)
        self.assertEqual(cost, 1500)
        
    def test_is_eligible(self):
        """Тест возможности экспресс-доставки."""
        express = ExpressDelivery("EXP001", 24)
        self.assertTrue(express.is_eligible(1000))
        self.assertFalse(express.is_eligible(3000))


class TestCustomsService(unittest.TestCase):
    """Тесты для класса CustomsService."""
    
    def test_file_declaration(self):
        """Тест подачи декларации."""
        customs = CustomsService()
        shipment = {'id': 'SHP001'}
        declaration = customs.file_declaration(shipment, 10000)
        self.assertEqual(declaration['status'], 'pending')
        
    def test_approve_declaration(self):
        """Тест одобрения декларации."""
        customs = CustomsService()
        shipment = {'id': 'SHP001'}
        declaration = customs.file_declaration(shipment, 10000)
        customs.approve_declaration(declaration)
        self.assertEqual(declaration['status'], 'approved')
        
    def test_calculate_duties(self):
        """Тест расчета пошлин."""
        customs = CustomsService()
        duties = customs.calculate_duties(10000, 0.1)
        self.assertEqual(duties, 1100)


class TestWarehouseService(unittest.TestCase):
    """Тесты для класса WarehouseService."""
    
    def test_store_goods(self):
        """Тест размещения товаров."""
        service = WarehouseService(10.0)
        service.store_goods("ITEM001", 100, 30)
        self.assertTrue("ITEM001" in service.stored_items)
        
    def test_calculate_storage_cost(self):
        """Тест расчета стоимости хранения."""
        service = WarehouseService(10.0)
        service.store_goods("ITEM001", 100, 30)
        cost = service.calculate_storage_cost("ITEM001")
        self.assertEqual(cost, 30000)
        
    def test_retrieve_goods(self):
        """Тест забора товаров."""
        service = WarehouseService(10.0)
        service.store_goods("ITEM001", 100, 30)
        result = service.retrieve_goods("ITEM001")
        self.assertTrue(result)
        self.assertTrue("ITEM001" not in service.stored_items)


class TestPackagingService(unittest.TestCase):
    """Тесты для класса PackagingService."""
    
    def test_calculate_packaging_cost(self):
        """Тест расчета стоимости упаковки."""
        service = PackagingService()
        cost = service.calculate_packaging_cost("standard", 10)
        self.assertEqual(cost, 50)
        
    def test_add_packaging_type(self):
        """Тест добавления типа упаковки."""
        service = PackagingService()
        service.add_packaging_type("custom", 30.0)
        self.assertTrue("custom" in service.packaging_types)


class TestInsuranceService(unittest.TestCase):
    """Тесты для класса InsuranceService."""
    
    def test_create_policy(self):
        """Тест создания полиса."""
        service = InsuranceService()
        shipment = {'id': 'SHP001'}
        policy = service.create_policy(shipment, 100000)
        self.assertEqual(policy['premium'], 2000)
        self.assertTrue(policy['is_active'])
        
    def test_file_claim(self):
        """Тест подачи претензии."""
        service = InsuranceService()
        shipment = {'id': 'SHP001'}
        policy = service.create_policy(shipment, 100000)
        claim = service.file_claim(policy, 50000)
        self.assertTrue(claim['approved'])
        self.assertEqual(claim['payout'], 50000)


class TestCustomerSupport(unittest.TestCase):
    """Тесты для класса CustomerSupport."""
    
    def test_create_ticket(self):
        """Тест создания тикета."""
        support = CustomerSupport()
        ticket = support.create_ticket("Customer1", "delivery_issue", "Package delayed")
        self.assertEqual(ticket['status'], 'open')
        self.assertEqual(len(support.tickets), 1)
        
    def test_resolve_ticket(self):
        """Тест решения тикета."""
        support = CustomerSupport()
        ticket = support.create_ticket("Customer1", "delivery_issue", "Package delayed")
        result = support.resolve_ticket(ticket['ticket_id'])
        self.assertTrue(result)
        self.assertEqual(ticket['status'], 'resolved')
        
    def test_get_open_tickets(self):
        """Тест получения открытых тикетов."""
        support = CustomerSupport()
        support.create_ticket("Customer1", "issue1", "Description1")
        support.create_ticket("Customer2", "issue2", "Description2")
        ticket = support.create_ticket("Customer3", "issue3", "Description3")
        support.resolve_ticket(ticket['ticket_id'])
        open_tickets = support.get_open_tickets()
        self.assertEqual(len(open_tickets), 2)


class TestSubscriptionService(unittest.TestCase):
    """Тесты для класса SubscriptionService."""
    
    def test_subscribe(self):
        """Тест подписки."""
        service = SubscriptionService("Premium", 99.99, ["benefit1", "benefit2"])
        subscription = service.subscribe("Customer1")
        self.assertTrue(subscription['is_active'])
        self.assertEqual(len(service.subscribers), 1)
        
    def test_cancel_subscription(self):
        """Тест отмены подписки."""
        service = SubscriptionService("Premium", 99.99, ["benefit1"])
        subscription = service.subscribe("Customer1")
        result = service.cancel_subscription("Customer1")
        self.assertTrue(result)
        self.assertFalse(subscription['is_active'])
        
    def test_get_active_subscribers_count(self):
        """Тест получения количества активных подписчиков."""
        service = SubscriptionService("Premium", 99.99, ["benefit1"])
        service.subscribe("Customer1")
        service.subscribe("Customer2")
        subscription = service.subscribe("Customer3")
        service.cancel_subscription("Customer3")
        count = service.get_active_subscribers_count()
        self.assertEqual(count, 2)
