"""
Юнит-тесты для модуля staffперсонал.
"""

import unittest
from datetime import datetime, timedelta
from logisticsApp.logistics.staff import Employee, Driver, WarehouseWorker, Dispatcher, Manager, Department
from logisticsApp.logistics.vehicles import Vehicle
from logisticsApp.logistics.warehouses import Warehouse


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""
    
    def test_assign_department(self):
        """Тест назначения в отдел."""
        employee = Employee("E001", "John", "engineer", 50000)
        department = Department("Engineering", 100000)
        employee.assign_department(department)
        self.assertEqual(employee.department, department)
        
    def test_terminate(self):
        """Тест увольнения."""
        employee = Employee("E001", "John", "engineer", 50000)
        employee.terminate()
        self.assertFalse(employee.is_active)
        
    def test_give_raise(self):
        """Тест повышения зарплаты."""
        employee = Employee("E001", "John", "engineer", 50000)
        employee.give_raise(5000)
        self.assertEqual(employee.salary, 55000)


class TestDriver(unittest.TestCase):
    """Тесты для класса Driver."""
    
    def test_assign_vehicle(self):
        """Тест назначения транспорта."""
        driver = Driver("D001", "John", 60000, "C")
        vehicle = Vehicle("V001", "truck", 10000, "diesel")
        driver.assign_vehicle(vehicle)
        self.assertEqual(driver.assigned_vehicle, vehicle)
        
    def test_complete_delivery(self):
        """Тест завершения доставки."""
        driver = Driver("D001", "John", 60000, "C")
        driver.complete_delivery(150)
        self.assertEqual(driver.deliveries_completed, 1)
        self.assertEqual(driver.total_distance_km, 150)
        
    def test_is_license_valid(self):
        """Тест проверки лицензии."""
        driver = Driver("D001", "John", 60000, "C")
        self.assertTrue(driver.is_license_valid())
        
    def test_renew_license(self):
        """Тест продления лицензии."""
        driver = Driver("D001", "John", 60000, "C")
        old_expiry = driver.license_expiry
        driver.renew_license(3)
        self.assertTrue(driver.license_expiry > old_expiry)


class TestWarehouseWorker(unittest.TestCase):
    """Тесты для класса WarehouseWorker."""
    
    def test_assign_warehouse(self):
        """Тест назначения на склад."""
        worker = WarehouseWorker("W001", "Anna", 50000, "day")
        warehouse = Warehouse("WH001", "Main", "Moscow", 1000)
        worker.assign_warehouse(warehouse)
        self.assertEqual(worker.assigned_warehouse, warehouse)
        
    def test_process_items(self):
        """Тест обработки товаров."""
        worker = WarehouseWorker("W001", "Anna", 50000, "day")
        worker.process_items(50)
        self.assertEqual(worker.items_processed, 50)
        
    def test_certify_forklift(self):
        """Тест получения сертификата."""
        worker = WarehouseWorker("W001", "Anna", 50000, "day")
        worker.certify_forklift()
        self.assertTrue(worker.forklift_certified)


class TestDispatcher(unittest.TestCase):
    """Тесты для класса Dispatcher."""
    
    def test_assign_route(self):
        """Тест назначения маршрута."""
        dispatcher = Dispatcher("D001", "Maria", 55000)
        route = {'id': 'R001', 'destination': 'SPB'}
        dispatcher.assign_route(route)
        self.assertEqual(len(dispatcher.assigned_routes), 1)
        
    def test_handle_call(self):
        """Тест обработки звонка."""
        dispatcher = Dispatcher("D001", "Maria", 55000)
        dispatcher.handle_call()
        self.assertEqual(dispatcher.calls_handled, 1)


class TestManager(unittest.TestCase):
    """Тесты для класса Manager."""
    
    def test_add_team_member(self):
        """Тест добавления члена команды."""
        manager = Manager("M001", "Alex", 100000, 5)
        employee = Employee("E001", "John", "engineer", 50000)
        manager.add_team_member(employee)
        self.assertEqual(len(manager.team_members), 1)
        
    def test_remove_team_member(self):
        """Тест удаления члена команды."""
        manager = Manager("M001", "Alex", 100000, 5)
        employee = Employee("E001", "John", "engineer", 50000)
        manager.add_team_member(employee)
        manager.remove_team_member(employee)
        self.assertEqual(len(manager.team_members), 0)
        
    def test_complete_project(self):
        """Тест завершения проекта."""
        manager = Manager("M001", "Alex", 100000, 5)
        manager.complete_project()
        self.assertEqual(manager.projects_completed, 1)


class TestDepartment(unittest.TestCase):
    """Тесты для класса Department."""
    
    def test_add_employee(self):
        """Тест добавления сотрудника."""
        department = Department("Engineering", 100000)
        employee = Employee("E001", "John", "engineer", 50000)
        department.add_employee(employee)
        self.assertEqual(len(department.employees), 1)
        self.assertEqual(employee.department, department)
        
    def test_remove_employee(self):
        """Тест удаления сотрудника."""
        department = Department("Engineering", 100000)
        employee = Employee("E001", "John", "engineer", 50000)
        department.add_employee(employee)
        department.remove_employee(employee)
        self.assertEqual(len(department.employees), 0)
        
    def test_assign_manager(self):
        """Тест назначения менеджера."""
        department = Department("Engineering", 100000)
        manager = Manager("M001", "Alex", 100000, 5)
        department.assign_manager(manager)
        self.assertEqual(department.manager, manager)
        
    def test_get_total_payroll(self):
        """Тест получения фонда зарплаты."""
        department = Department("Engineering", 100000)
        e1 = Employee("E001", "John", "engineer", 50000)
        e2 = Employee("E002", "Jane", "engineer", 60000)
        department.add_employee(e1)
        department.add_employee(e2)
        self.assertEqual(department.get_total_payroll(), 110000)
        
    def test_get_employee_count(self):
        """Тест получения количества сотрудников."""
        department = Department("Engineering", 100000)
        e1 = Employee("E001", "John", "engineer", 50000)
        e2 = Employee("E002", "Jane", "engineer", 60000)
        department.add_employee(e1)
        department.add_employee(e2)
        self.assertEqual(department.get_employee_count(), 2)
