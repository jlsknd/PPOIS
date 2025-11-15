"""
Юнит-тесты для модуля транспортных средств.
"""

import unittest
from datetime import datetime, timedelta
from logisticsApp.logistics.vehicles import Vehicle, Truck, Van, Container, Fleet
from logisticsApp.logistics.exceptions import VehicleUnavailableError, OverweightError


class TestVehicle(unittest.TestCase):
    """Тесты для класса Vehicle."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.vehicle = Vehicle("V001", "truck", 10000, "diesel")
    
    def test_load_cargo(self):
        """Тест загрузки груза."""
        self.vehicle.load_cargo(5000)
        self.assertEqual(self.vehicle.current_load, 5000)
        
    def test_load_cargo_overweight(self):
        """Тест превышения грузоподъемности."""
        with self.assertRaises(OverweightError):
            self.vehicle.load_cargo(15000)
            
    def test_unload_cargo(self):
        """Тест выгрузки груза."""
        self.vehicle.load_cargo(5000)
        self.vehicle.unload_cargo(3000)
        self.assertEqual(self.vehicle.current_load, 2000)
        
    def test_set_unavailable(self):
        """Тест установки недоступности."""
        self.vehicle.set_unavailable()
        self.assertFalse(self.vehicle.is_available)
        
    def test_schedule_maintenance(self):
        """Тест планирования обслуживания."""
        date = self.vehicle.schedule_maintenance()
        self.assertFalse(self.vehicle.is_available)
        self.assertGreater(date, datetime.now())
        
    def test_complete_maintenance(self):
        """Тест завершения обслуживания."""
        self.vehicle.schedule_maintenance()
        self.vehicle.complete_maintenance()
        self.assertTrue(self.vehicle.is_available)
        
    def test_add_mileage(self):
        """Тест добавления пробега."""
        self.vehicle.add_mileage(100)
        self.assertEqual(self.vehicle.mileage, 100)
        
    def test_get_available_capacity(self):
        """Тест получения доступной грузоподъемности."""
        self.vehicle.load_cargo(3000)
        self.assertEqual(self.vehicle.get_available_capacity(), 7000)


class TestTruck(unittest.TestCase):
    """Тесты для класса Truck."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.truck = Truck("T001", 10000)
    
    def test_attach_trailer(self):
        """Тест прицепа прицепа."""
        initial_capacity = self.truck.capacity_kg
        self.truck.attach_trailer()
        self.assertTrue(self.truck.trailer_attached)
        self.assertEqual(self.truck.capacity_kg, initial_capacity * 1.5)
        
    def test_detach_trailer(self):
        """Тест отцепа прицепа."""
        self.truck.attach_trailer()
        self.truck.detach_trailer()
        self.assertFalse(self.truck.trailer_attached)


class TestVan(unittest.TestCase):
    """Тесты для класса Van."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.van = Van("V001", 2000)
    
    def test_volume_calculation(self):
        """Тест расчета объема."""
        self.assertEqual(self.van.volume_m3, 10)


class TestContainer(unittest.TestCase):
    """Тесты для класса Container."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.container = Container("C001", "20ft", 20000)
    
    def test_add_cargo(self):
        """Тест добавления груза."""
        cargo = {'name': 'Electronics', 'weight': 5000}
        self.container.add_cargo(cargo)
        self.assertEqual(len(self.container.contents), 1)
        self.assertEqual(self.container.current_weight, 5000)
        
    def test_add_cargo_overweight(self):
        """Тест превышения веса контейнера."""
        cargo = {'name': 'Heavy', 'weight': 25000}
        with self.assertRaises(OverweightError):
            self.container.add_cargo(cargo)
            
    def test_seal_container(self):
        """Тест опечатывания контейнера."""
        self.container.seal_container()
        self.assertTrue(self.container.is_sealed)
        
    def test_unseal_container(self):
        """Тест распечатывания контейнера."""
        self.container.seal_container()
        self.container.unseal_container()
        self.assertFalse(self.container.is_sealed)


class TestFleet(unittest.TestCase):
    """Тесты для класса Fleet."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.fleet = Fleet("Test Fleet")
    
    def test_add_vehicle(self):
        """Тест добавления транспорта."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        self.fleet.add_vehicle(vehicle)
        self.assertEqual(len(self.fleet.vehicles), 1)
        self.assertEqual(self.fleet.total_capacity, 10000)
        
    def test_remove_vehicle(self):
        """Тест удаления транспорта."""
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        self.fleet.add_vehicle(vehicle)
        self.fleet.remove_vehicle(vehicle)
        self.assertEqual(len(self.fleet.vehicles), 0)
        
    def test_get_available_vehicles(self):
        """Тест получения доступных транспортных средств."""
        v1 = Vehicle("V001", "truck", 10000, "diesel")
        v2 = Vehicle("V002", "truck", 10000, "diesel")
        v2.set_unavailable()
        self.fleet.add_vehicle(v1)
        self.fleet.add_vehicle(v2)
        available = self.fleet.get_available_vehicles()
        self.assertEqual(len(available), 1)
        
    def test_find_vehicle_by_capacity(self):
        """Тест поиска транспорта по грузоподъемности."""
        v1 = Vehicle("V001", "truck", 10000, "diesel")
        self.fleet.add_vehicle(v1)
        found = self.fleet.find_vehicle_by_capacity(5000)
        self.assertEqual(found, v1)
        
    def test_get_fleet_utilization(self):
        """Тест получения коэффициента использования парка."""
        v1 = Vehicle("V001", "truck", 10000, "diesel")
        v2 = Vehicle("V002", "truck", 10000, "diesel")
        v2.set_unavailable()
        self.fleet.add_vehicle(v1)
        self.fleet.add_vehicle(v2)
        utilization = self.fleet.get_fleet_utilization()
        self.assertEqual(utilization, 50.0)
