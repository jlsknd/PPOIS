"""
Юнит-тесты для модуля infrastructureинфраструктура.
"""

import unittest
from datetime import datetime
from logisticsApp.logistics.infrastructure import LogisticsCenter, SecuritySystem, Camera, AccessControl, GPSTracker, MaintenanceSchedule, LoadingSchedule
from logisticsApp.logistics.exceptions import InsufficientCapacityError, UnauthorizedAccessError


class TestLogisticsCenter(unittest.TestCase):
    """Тесты для класса LogisticsCenter."""
    
    def test_open_center(self):
        """Тест открытия центра."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        center.open_center()
        self.assertTrue(center.is_operational)
        
    def test_close_center(self):
        """Тест закрытия центра."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        center.open_center()
        center.close_center()
        self.assertFalse(center.is_operational)
        
    def test_add_warehouse(self):
        """Тест добавления склада."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        warehouse = {'id': 'WH001'}
        center.add_warehouse(warehouse)
        self.assertEqual(len(center.warehouses), 1)
        
    def test_admit_vehicle(self):
        """Тест впуска транспорта."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        center.open_center()
        center.admit_vehicle()
        self.assertEqual(center.vehicles_count, 1)
        
    def test_admit_vehicle_closed(self):
        """Тест впуска при закрытом центре."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        with self.assertRaises(InsufficientCapacityError):
            center.admit_vehicle()
            
    def test_release_vehicle(self):
        """Тест выпуска транспорта."""
        center = LogisticsCenter("Main Hub", "Moscow", 100)
        center.open_center()
        center.admit_vehicle()
        center.release_vehicle()
        self.assertEqual(center.vehicles_count, 0)


class TestSecuritySystem(unittest.TestCase):
    """Тесты для класса SecuritySystem."""
    
    def test_add_camera(self):
        """Тест добавления камеры."""
        security = SecuritySystem()
        camera = Camera("CAM001", "Entrance")
        security.add_camera(camera)
        self.assertEqual(len(security.cameras), 1)
        
    def test_arm_system(self):
        """Тест активации системы."""
        security = SecuritySystem()
        security.arm_system()
        self.assertTrue(security.is_armed)
        
    def test_disarm_system(self):
        """Тест деактивации системы."""
        security = SecuritySystem()
        security.arm_system()
        security.disarm_system()
        self.assertFalse(security.is_armed)
        
    def test_trigger_alarm(self):
        """Тест включения тревоги."""
        security = SecuritySystem()
        security.trigger_alarm("Intrusion detected")
        self.assertTrue(security.alarm_triggered)
        
    def test_log_access(self):
        """Тест записи доступа."""
        security = SecuritySystem()
        security.log_access("USER001", "Warehouse A")
        self.assertEqual(len(security.access_logs), 1)


class TestCamera(unittest.TestCase):
    """Тесты для класса Camera."""
    
    def test_start_recording(self):
        """Тест начала записи."""
        camera = Camera("CAM001", "Entrance")
        camera.start_recording()
        self.assertTrue(camera.is_recording)
        
    def test_stop_recording(self):
        """Тест остановки записи."""
        camera = Camera("CAM001", "Entrance")
        camera.start_recording()
        camera.stop_recording()
        self.assertFalse(camera.is_recording)
        
    def test_save_footage(self):
        """Тест сохранения записи."""
        camera = Camera("CAM001", "Entrance")
        camera.save_footage("video_data")
        self.assertEqual(len(camera.footage), 1)


class TestAccessControl(unittest.TestCase):
    """Тесты для класса AccessControl."""
    
    def test_authorize_user(self):
        """Тест авторизации пользователя."""
        access_control = AccessControl()
        access_control.authorize_user("USER001", ["Zone A", "Zone B"])
        self.assertTrue("USER001" in access_control.authorized_users)
        
    def test_revoke_access(self):
        """Тест отзыва доступа."""
        access_control = AccessControl()
        access_control.authorize_user("USER001", ["Zone A"])
        access_control.revoke_access("USER001")
        self.assertTrue("USER001" not in access_control.authorized_users)
        
    def test_check_access_authorized(self):
        """Тест проверки разрешенного доступа."""
        access_control = AccessControl()
        access_control.authorize_user("USER001", ["Zone A"])
        result = access_control.check_access("USER001", "Zone A")
        self.assertTrue(result)
        
    def test_check_access_unauthorized_user(self):
        """Тест проверки неавторизованного пользователя."""
        access_control = AccessControl()
        with self.assertRaises(UnauthorizedAccessError):
            access_control.check_access("USER001", "Zone A")
            
    def test_check_access_unauthorized_zone(self):
        """Тест проверки доступа к неразрешенной зоне."""
        access_control = AccessControl()
        access_control.authorize_user("USER001", ["Zone A"])
        with self.assertRaises(UnauthorizedAccessError):
            access_control.check_access("USER001", "Zone B")


class TestGPSTracker(unittest.TestCase):
    """Тесты для класса GPSTracker."""
    
    def test_update_location(self):
        """Тест обновления местоположения."""
        tracker = GPSTracker("GPS001")
        tracker.update_location(55.7558, 37.6173)
        self.assertTrue(tracker.current_location is not None)
        self.assertEqual(len(tracker.location_history), 1)
        
    def test_get_current_location(self):
        """Тест получения текущего местоположения."""
        tracker = GPSTracker("GPS001")
        tracker.update_location(55.7558, 37.6173)
        location = tracker.get_current_location()
        self.assertEqual(location['latitude'], 55.7558)
        
    def test_deactivate(self):
        """Тест деактивации трекера."""
        tracker = GPSTracker("GPS001")
        tracker.deactivate()
        self.assertFalse(tracker.is_active)


class TestMaintenanceSchedule(unittest.TestCase):
    """Тесты для класса MaintenanceSchedule."""
    
    def test_schedule_maintenance(self):
        """Тест планирования обслуживания."""
        schedule = MaintenanceSchedule()
        schedule.schedule_maintenance("V001", datetime.now(), "oil_change")
        self.assertEqual(len(schedule.scheduled_maintenance), 1)
        
    def test_complete_maintenance(self):
        """Тест завершения обслуживания."""
        schedule = MaintenanceSchedule()
        schedule.schedule_maintenance("V001", datetime.now(), "oil_change")
        schedule.complete_maintenance("V001")
        self.assertEqual(schedule.scheduled_maintenance[0]['status'], "completed")
        
    def test_get_upcoming_maintenance(self):
        """Тест получения предстоящих обслуживаний."""
        schedule = MaintenanceSchedule()
        schedule.schedule_maintenance("V001", datetime.now(), "oil_change")
        schedule.schedule_maintenance("V002", datetime.now(), "inspection")
        schedule.complete_maintenance("V001")
        upcoming = schedule.get_upcoming_maintenance()
        self.assertEqual(len(upcoming), 1)


class TestLoadingSchedule(unittest.TestCase):
    """Тесты для класса LoadingSchedule."""
    
    def test_schedule_loading(self):
        """Тест планирования погрузки."""
        schedule = LoadingSchedule()
        operation_id = schedule.schedule_loading("V001", "DOCK1", datetime.now(), ["cargo1", "cargo2"])
        self.assertIsNotNone(operation_id)
        self.assertEqual(len(schedule.scheduled_operations), 1)
        
    def test_start_operation(self):
        """Тест начала операции погрузки."""
        schedule = LoadingSchedule()
        operation_id = schedule.schedule_loading("V001", "DOCK1", datetime.now(), ["cargo1"])
        result = schedule.start_operation(operation_id)
        self.assertTrue(result)
        self.assertEqual(schedule.scheduled_operations[0]['status'], "in_progress")
        
    def test_complete_operation(self):
        """Тест завершения операции погрузки."""
        schedule = LoadingSchedule()
        operation_id = schedule.schedule_loading("V001", "DOCK1", datetime.now(), ["cargo1"])
        schedule.start_operation(operation_id)
        result = schedule.complete_operation(operation_id)
        self.assertTrue(result)
        self.assertEqual(len(schedule.completed_operations), 1)
        self.assertEqual(len(schedule.scheduled_operations), 0)
        
    def test_get_operations_by_dock(self):
        """Тест получения операций для конкретной платформы."""
        schedule = LoadingSchedule()
        schedule.schedule_loading("V001", "DOCK1", datetime.now(), ["cargo1"])
        schedule.schedule_loading("V002", "DOCK2", datetime.now(), ["cargo2"])
        schedule.schedule_loading("V003", "DOCK1", datetime.now(), ["cargo3"])
        operations = schedule.get_operations_by_dock("DOCK1")
        self.assertEqual(len(operations), 2)
        
    def test_get_operations_by_status(self):
        """Тест получения операций по статусу."""
        schedule = LoadingSchedule()
        op1 = schedule.schedule_loading("V001", "DOCK1", datetime.now(), ["cargo1"])
        op2 = schedule.schedule_loading("V002", "DOCK2", datetime.now(), ["cargo2"])
        schedule.start_operation(op1)
        scheduled = schedule.get_operations_by_status("scheduled")
        in_progress = schedule.get_operations_by_status("in_progress")
        self.assertEqual(len(scheduled), 1)
        self.assertEqual(len(in_progress), 1)
