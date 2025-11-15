class AccessControl:
    """Класс контроля доступа."""
    
    def __init__(self):
        """Инициализация контроля доступа."""
        self.authorized_users = {}
        self.access_zones = {}
        
    def authorize_user(self, user_id, zones):
        """Авторизовать пользователя."""
        self.authorized_users[user_id] = zones
        
    def revoke_access(self, user_id):
        """Отозвать доступ."""
        if user_id in self.authorized_users:
            del self.authorized_users[user_id]
            
    def check_access(self, user_id, zone):
        """Проверить доступ."""
        if user_id not in self.authorized_users:
            from museum.exceptions import UnauthorizedAccessError
            raise UnauthorizedAccessError("Пользователь не авторизован")
        if zone not in self.authorized_users[user_id]:
            from museum.exceptions import UnauthorizedAccessError
            raise UnauthorizedAccessError(f"Доступ к зоне {zone} запрещен")
        return True
        
    def add_zone(self, zone_name, security_level):
        """Добавить зону."""
        self.access_zones[zone_name] = security_level
