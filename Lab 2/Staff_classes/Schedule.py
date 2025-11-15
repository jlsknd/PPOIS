class Schedule:
    """Класс расписания работы."""
    
    def __init__(self, employee):
        """
        Инициализация расписания.
        
        Args:
            employee: Сотрудник
        """
        self.employee = employee
        self.shifts = []
        self.days_off = []
        
    def add_shift(self, day, start_time, end_time):
        """Добавить смену."""
        self.shifts.append({
            'day': day,
            'start': start_time,
            'end': end_time
        })
        
    def add_day_off(self, date):
        """Добавить выходной."""
        self.days_off.append(date)
        
    def get_weekly_hours(self):
        """Получить недельные часы."""
        return len(self.shifts) * 8
        
    def is_working(self, day):
        """Проверить работает ли в день."""
        return any(s['day'] == day for s in self.shifts)
