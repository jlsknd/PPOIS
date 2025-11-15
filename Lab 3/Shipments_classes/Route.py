class Route:
    """Класс маршрута."""
    
    def __init__(self, route_id, start_point, end_point, distance_km):
        """
        Инициализация маршрута.
        
        Args:
            route_id: ID маршрута
            start_point: Точка отправления
            end_point: Точка назначения
            distance_km: Расстояние в км
        """
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.distance_km = distance_km
        self.waypoints = []
        self.estimated_time_hours = distance_km / 60  # Средняя скорость 60 км/ч
        self.traffic_conditions = "normal"
        self.road_type = "highway"
        
    def add_waypoint(self, waypoint):
        """Добавить промежуточную точку."""
        self.waypoints.append(waypoint)
        
    def calculate_fuel_cost(self, fuel_price_per_liter, consumption_per_100km):
        """Рассчитать стоимость топлива."""
        fuel_needed = (self.distance_km / 100) * consumption_per_100km
        return fuel_needed * fuel_price_per_liter
        
    def get_total_stops(self):
        """Получить количество остановок."""
        return len(self.waypoints)
        
    def optimize_route(self):
        """Оптимизировать маршрут."""
        # Простая оптимизация - сортировка точек
        if self.waypoints:
            self.waypoints.sort(key=lambda x: x.get('priority', 0), reverse=True)
