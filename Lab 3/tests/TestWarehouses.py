"""
Юнит-тесты для модуля warehousesсклады.
"""

import unittest
from logisticsApp.logistics.warehouses import Warehouse, StorageZone, Inventory, LoadingDock
from logisticsApp.logistics.exceptions import InsufficientCapacityError


class TestWarehouse(unittest.TestCase):
    """Тесты для класса Warehouse."""
    
    def test_store_item(self):
        """Тест размещения товара."""
        warehouse = Warehouse("W001", "Main", "Moscow", 1000)
        item = {'name': 'Box', 'volume_m3': 10, 'quantity': 5}
        warehouse.store_item("ITEM001", item)
        self.assertTrue("ITEM001" in warehouse.inventory)
        self.assertEqual(warehouse.occupied_space, 10)
        
    def test_store_item_insufficient_capacity(self):
        """Тест превышения вместимости."""
        warehouse = Warehouse("W001", "Main", "Moscow", 100)
        item = {'name': 'Box', 'volume_m3': 150, 'quantity': 5}
        with self.assertRaises(InsufficientCapacityError):
            warehouse.store_item("ITEM001", item)
            
    def test_retrieve_item(self):
        """Тест извлечения товара."""
        warehouse = Warehouse("W001", "Main", "Moscow", 1000)
        item = {'name': 'Box', 'volume_m3': 10, 'quantity': 5}
        warehouse.store_item("ITEM001", item)
        result = warehouse.retrieve_item("ITEM001", 2)
        self.assertTrue(result)
        self.assertEqual(warehouse.inventory["ITEM001"]['quantity'], 3)
        
    def test_get_available_space(self):
        """Тест получения доступного пространства."""
        warehouse = Warehouse("W001", "Main", "Moscow", 1000)
        item = {'name': 'Box', 'volume_m3': 100, 'quantity': 1}
        warehouse.store_item("ITEM001", item)
        self.assertEqual(warehouse.get_available_space(), 900)
        
    def test_get_occupancy_rate(self):
        """Тест получения процента заполненности."""
        warehouse = Warehouse("W001", "Main", "Moscow", 1000)
        item = {'name': 'Box', 'volume_m3': 250, 'quantity': 1}
        warehouse.store_item("ITEM001", item)
        self.assertEqual(warehouse.get_occupancy_rate(), 25.0)
        
    def test_find_item(self):
        """Тест поиска товара."""
        warehouse = Warehouse("W001", "Main", "Moscow", 1000)
        item = {'name': 'Box', 'volume_m3': 10, 'quantity': 5}
        warehouse.store_item("ITEM001", item)
        found = warehouse.find_item("ITEM001")
        self.assertTrue(found is not None)


class TestStorageZone(unittest.TestCase):
    """Тесты для класса StorageZone."""
    
    def test_add_item(self):
        """Тест добавления товара в зону."""
        zone = StorageZone("Z001", "ambient", 10)
        zone.add_item({'name': 'Box'})
        self.assertEqual(len(zone.items), 1)
        
    def test_add_item_full(self):
        """Тест добавления в заполненную зону."""
        zone = StorageZone("Z001", "ambient", 1)
        zone.add_item({'name': 'Box1'})
        with self.assertRaises(InsufficientCapacityError):
            zone.add_item({'name': 'Box2'})
            
    def test_remove_item(self):
        """Тест удаления товара из зоны."""
        zone = StorageZone("Z001", "ambient", 10)
        item = {'name': 'Box'}
        zone.add_item(item)
        zone.remove_item(item)
        self.assertEqual(len(zone.items), 0)
        
    def test_set_temperature(self):
        """Тест установки температуры."""
        zone = StorageZone("Z001", "refrigerated", 10)
        zone.set_temperature(-5)
        self.assertEqual(zone.temperature, -5)
        
    def test_is_full(self):
        """Тест проверки заполненности."""
        zone = StorageZone("Z001", "ambient", 1)
        zone.add_item({'name': 'Box'})
        self.assertTrue(zone.is_full())


class TestInventory(unittest.TestCase):
    """Тесты для класса Inventory."""
    
    def test_add_stock(self):
        """Тест добавления запасов."""
        inventory = Inventory()
        inventory.add_stock("ITEM001", 100, {'name': 'Product A'})
        self.assertEqual(inventory.get_stock_level("ITEM001"), 100)
        
    def test_remove_stock(self):
        """Тест убирания запасов."""
        inventory = Inventory()
        inventory.add_stock("ITEM001", 100, {'name': 'Product A'})
        result = inventory.remove_stock("ITEM001", 30)
        self.assertTrue(result)
        self.assertEqual(inventory.get_stock_level("ITEM001"), 70)
        
    def test_check_low_stock(self):
        """Тест проверки низких запасов."""
        inventory = Inventory()
        inventory.add_stock("ITEM001", 5, {'name': 'Product A'})
        inventory.add_stock("ITEM002", 20, {'name': 'Product B'})
        low_stock = inventory.check_low_stock()
        self.assertTrue("ITEM001" in low_stock)
        self.assertTrue("ITEM002" not in low_stock)
        
    def test_get_total_items(self):
        """Тест получения общего количества товаров."""
        inventory = Inventory()
        inventory.add_stock("ITEM001", 100, {'name': 'Product A'})
        inventory.add_stock("ITEM002", 200, {'name': 'Product B'})
        self.assertEqual(inventory.get_total_items(), 300)


class TestLoadingDock(unittest.TestCase):
    """Тесты для класса LoadingDock."""
    
    def test_assign_vehicle(self):
        """Тест назначения транспорта."""
        dock = LoadingDock("D001", 3)
        dock.is_operational = True
        vehicle = {'id': 'V001'}
        dock.assign_vehicle(vehicle)
        self.assertEqual(len(dock.current_vehicles), 1)
        
    def test_assign_vehicle_full(self):
        """Тест назначения при заполненности."""
        dock = LoadingDock("D001", 1)
        dock.is_operational = True
        dock.assign_vehicle({'id': 'V001'})
        with self.assertRaises(InsufficientCapacityError):
            dock.assign_vehicle({'id': 'V002'})
            
    def test_release_vehicle(self):
        """Тест освобождения транспорта."""
        dock = LoadingDock("D001", 3)
        dock.is_operational = True
        vehicle = {'id': 'V001'}
        dock.assign_vehicle(vehicle)
        dock.release_vehicle(vehicle)
        self.assertEqual(len(dock.current_vehicles), 0)
        
    def test_get_available_spots(self):
        """Тест получения свободных мест."""
        dock = LoadingDock("D001", 5)
        dock.is_operational = True
        dock.assign_vehicle({'id': 'V001'})
        dock.assign_vehicle({'id': 'V002'})
        self.assertEqual(dock.get_available_spots(), 3)
        
    def test_close_dock(self):
        """Тест закрытия платформы."""
        dock = LoadingDock("D001", 3)
        dock.close_dock()
        self.assertFalse(dock.is_operational)
        
    def test_open_dock(self):
        """Тест открытия платформы."""
        dock = LoadingDock("D001", 3)
        dock.close_dock()
        dock.open_dock()
        self.assertTrue(dock.is_operational)
