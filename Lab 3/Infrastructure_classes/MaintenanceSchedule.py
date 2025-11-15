class MaintenanceSchedule:
    """Класс графика обслуживания."""
    
    def __init__(self):
        """Инициализация графика обслуживания."""
        self.scheduled_maintenance = []
        
    def schedule_maintenance(self, vehicle_id, date, maintenance_type):
        """Запланировать обслуживание."""
        self.scheduled_maintenance.append({
            'vehicle_id': vehicle_id,
            'date': date,
            'type': maintenance_type,
            'status': 'scheduled'
        })
        
    def complete_maintenance(self, vehicle_id):
        """Завершить обслуживание."""
        for maintenance in self.scheduled_maintenance:
            if maintenance['vehicle_id'] == vehicle_id and maintenance['status'] == 'scheduled':
                maintenance['status'] = 'completed'
                maintenance['completed_date'] = datetime.now()
                break
                
    def get_upcoming_maintenance(self):
        """Получить предстоящие обслуживания."""
        return [m for m in self.scheduled_maintenance if m['status'] == 'scheduled']
