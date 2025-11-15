"""
Юнит-тесты для модуля shipmentsгрузоперевозки.
"""

import unittest
from datetime import datetime, timedelta
from logisticsApp.logistics.shipments import Shipment, Delivery, Route, TrackingSystem, Cargo
from logisticsApp.logistics.vehicles import Vehicle
from logisticsApp.logistics.staff import Driver
from logisticsApp.logistics.exceptions import ShipmentNotFoundError


class TestShipment(unittest.TestCase):
    """Тесты для класса Shipment."""
    
    def test_assign_tracking_number(self):
        """Тест присвоения трек-номера."""
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.assign_tracking_number("TRK123456")
        self.assertEqual(shipment.tracking_number, "TRK123456")
        
    def test_update_status(self):
        """Тест обновления статуса."""
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.update_status("in_transit")
        self.assertEqual(shipment.status, "in_transit")
        
    def test_mark_delivered(self):
        """Тест отметки о доставке."""
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.mark_delivered()
        self.assertEqual(shipment.status, "delivered")
        self.assertTrue(shipment.actual_delivery is not None)
        
    def test_update_location(self):
        """Тест обновления местоположения."""
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.update_location("Warehouse A")
        self.assertEqual(shipment.current_location, "Warehouse A")
        
    def test_is_delayed(self):
        """Тест проверки задержки."""
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.estimated_delivery = datetime.now() - timedelta(hours=1)
        self.assertTrue(shipment.is_delayed())


class TestDelivery(unittest.TestCase):
    """Тесты для класса Delivery."""
    
    def test_add_shipment(self):
        """Тест добавления груза."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver = Driver("D001", "John", 50000, "C")
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        delivery = Delivery("DEL001", [], vehicle, driver)
        delivery.add_shipment(shipment)
        self.assertEqual(len(delivery.shipments), 1)
        
    def test_assign_route(self):
        """Тест назначения маршрута."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver = Driver("D001", "John", 50000, "C")
        delivery = Delivery("DEL001", [], vehicle, driver)
        route = Route("R001", "Moscow", "SPB", 700)
        delivery.assign_route(route)
        self.assertEqual(delivery.route, route)
        
    def test_start_delivery(self):
        """Тест начала доставки."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver = Driver("D001", "John", 50000, "C")
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        delivery = Delivery("DEL001", shipment, vehicle, driver)
        delivery.start_delivery()
        self.assertEqual(delivery.status, "in_progress")
        self.assertFalse(vehicle.is_available)
        
    def test_complete_delivery(self):
        """Тест завершения доставки."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver = Driver("D001", "John", 50000, "C")
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        delivery = Delivery("DEL001", shipment, vehicle, driver)
        delivery.start_delivery()
        delivery.complete_delivery()
        self.assertEqual(delivery.status, "completed")
        self.assertTrue(vehicle.is_available)
        
    def test_get_total_weight(self):
        """Тест получения общего веса."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver = Driver("D001", "John", 50000, "C")
        s1 = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        s2 = Shipment("S002", "Sender", "Recipient", 2000, "SPB")
        delivery = Delivery("DEL001", [s1, s2], vehicle, driver)
        self.assertEqual(delivery.get_total_weight(), 3000)


class TestRoute(unittest.TestCase):
    """Тесты для класса Route."""
    
    def test_add_waypoint(self):
        """Тест добавления промежуточной точки."""
        route = Route("R001", "Moscow", "SPB", 700)
        route.add_waypoint({'name': 'Tver', 'priority': 1})
        self.assertEqual(len(route.waypoints), 1)
        
    def test_calculate_fuel_cost(self):
        """Тест расчета стоимости топлива."""
        route = Route("R001", "Moscow", "SPB", 700)
        cost = route.calculate_fuel_cost(50, 30)
        self.assertEqual(cost, 700 / 100 * 30 * 50)
        
    def test_get_total_stops(self):
        """Тест получения количества остановок."""
        route = Route("R001", "Moscow", "SPB", 700)
        route.add_waypoint({'name': 'Tver', 'priority': 1})
        route.add_waypoint({'name': 'Novgorod', 'priority': 2})
        self.assertEqual(route.get_total_stops(), 2)
        
    def test_optimize_route(self):
        """Тест оптимизации маршрута."""
        route = Route("R001", "Moscow", "SPB", 700)
        route.add_waypoint({'name': 'Tver', 'priority': 1})
        route.add_waypoint({'name': 'Novgorod', 'priority': 3})
        route.optimize_route()
        self.assertEqual(route.waypoints[0]['priority'], 3)


class TestTrackingSystem(unittest.TestCase):
    """Тесты для класса TrackingSystem."""
    
    def test_register_shipment(self):
        """Тест регистрации груза."""
        tracking = TrackingSystem()
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        tracking.register_shipment(shipment)
        self.assertTrue(shipment.tracking_number is not None)
        self.assertEqual(len(tracking.tracked_shipments), 1)
        
    def test_track_shipment(self):
        """Тест отслеживания груза."""
        tracking = TrackingSystem()
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        tracking.register_shipment(shipment)
        found = tracking.track_shipment(shipment.tracking_number)
        self.assertEqual(found, shipment)
        
    def test_track_shipment_not_found(self):
        """Тест отслеживания несуществующего груза."""
        tracking = TrackingSystem()
        with self.assertRaises(ShipmentNotFoundError):
            tracking.track_shipment("INVALID")
            
    def test_get_shipments_by_status(self):
        """Тест получения грузов по статусу."""
        tracking = TrackingSystem()
        s1 = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        s2 = Shipment("S002", "Sender", "Recipient", 2000, "SPB")
        s1.update_status("in_transit")
        s2.update_status("delivered")
        tracking.register_shipment(s1)
        tracking.register_shipment(s2)
        in_transit = tracking.get_shipments_by_status("in_transit")
        self.assertEqual(len(in_transit), 1)
        
    def test_get_delayed_shipments(self):
        """Тест получения задержанных грузов."""
        tracking = TrackingSystem()
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        shipment.estimated_delivery = datetime.now() - timedelta(hours=1)
        tracking.register_shipment(shipment)
        delayed = tracking.get_delayed_shipments()
        self.assertEqual(len(delayed), 1)
        
    def test_update_shipment_location(self):
        """Тест обновления местоположения груза."""
        tracking = TrackingSystem()
        shipment = Shipment("S001", "Sender", "Recipient", 1000, "Moscow")
        tracking.register_shipment(shipment)
        tracking.update_shipment_location(shipment.tracking_number, "Warehouse B")
        self.assertEqual(shipment.current_location, "Warehouse B")


class TestCargo(unittest.TestCase):
    """Тесты для класса Cargo."""
    
    def test_mark_fragile(self):
        """Тест отметки груза как хрупкого."""
        cargo = Cargo("C001", "Стеклянная посуда", 5.0, {'length': 30, 'width': 20, 'height': 15})
        cargo.mark_fragile()
        self.assertTrue(cargo.is_fragile)
        
    def test_mark_hazardous(self):
        """Тест отметки груза как опасного."""
        cargo = Cargo("C002", "Химикаты", 10.0, {'length': 40, 'width': 30, 'height': 25})
        cargo.mark_hazardous()
        self.assertTrue(cargo.is_hazardous)
        
    def test_set_temperature_control(self):
        """Тест установки контроля температуры."""
        cargo = Cargo("C003", "Продукты питания", 15.0, {'length': 50, 'width': 40, 'height': 30})
        cargo.set_temperature_control(True)
        self.assertTrue(cargo.temperature_controlled)
        
    def test_assign_barcode(self):
        """Тест присвоения штрих-кода."""
        cargo = Cargo("C004", "Электроника", 8.0, {'length': 35, 'width': 25, 'height': 20})
        cargo.assign_barcode("BC123456789")
        self.assertEqual(cargo.barcode, "BC123456789")
        
    def test_calculate_volume(self):
        """Тест расчета объема груза."""
        cargo = Cargo("C005", "Мебель", 25.0, {'length': 100, 'width': 50, 'height': 40})
        volume = cargo.calculate_volume()
        self.assertEqual(volume, 0.2)  # 100*50*40 / 1000000 = 0.2 м³
