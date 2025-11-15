class LoadingSchedule:
    """Класс расписания погрузочных операций."""
    
    def __init__(self):
        """Инициализация расписания погрузки."""
        self.scheduled_operations = []
        self.completed_operations = []
        
    def schedule_loading(self, vehicle_id, dock_id, scheduled_time, cargo_list):
        """
        Запланировать погрузку.
        
        Args:
            vehicle_id: ID транспорта
            dock_id: ID погрузочной платформы
            scheduled_time: Запланированное время
            cargo_list: Список грузов для погрузки
        """
        operation = {
            'operation_id': f"LOAD{len(self.scheduled_operations):05d}",
            'vehicle_id': vehicle_id,
            'dock_id': dock_id,
            'scheduled_time': scheduled_time,
            'cargo_list': cargo_list,
            'status': 'scheduled',
            'actual_start': None,
            'actual_end': None
        }
        self.scheduled_operations.append(operation)
        return operation['operation_id']
        
    def start_operation(self, operation_id):
        """Начать операцию погрузки."""
        for op in self.scheduled_operations:
            if op['operation_id'] == operation_id and op['status'] == 'scheduled':
                op['status'] = 'in_progress'
                op['actual_start'] = datetime.now()
                return True
        return False
        
    def complete_operation(self, operation_id):
        """Завершить операцию погрузки."""
        for op in self.scheduled_operations:
            if op['operation_id'] == operation_id and op['status'] == 'in_progress':
                op['status'] = 'completed'
                op['actual_end'] = datetime.now()
                self.completed_operations.append(op)
                self.scheduled_operations.remove(op)
                return True
        return False
        
    def get_operations_by_dock(self, dock_id):
        """Получить операции для конкретной платформы."""
        return [op for op in self.scheduled_operations if op['dock_id'] == dock_id]
        
    def get_operations_by_status(self, status):
        """Получить операции по статусу."""
        return [op for op in self.scheduled_operations if op['status'] == status]
