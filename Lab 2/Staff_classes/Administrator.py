class Administrator:
    """Класс администратора."""
    
    def __init__(self, name, username, password):
        """
        Инициализация администратора.
        
        Args:
            name: Имя администратора
            username: Имя пользователя
            password: Пароль
        """
        self.name = name
        self.username = username
        self._password = password
        self.access_level = "admin"
        self.last_login = None
        
    def verify_password(self, password):
        """Проверить пароль."""
        if self._password != password:
            raise InvalidPasswordError("Неверный пароль")
        return True
        
    def change_password(self, old_password, new_password):
        """Сменить пароль."""
        self.verify_password(old_password)
        self._password = new_password
        
    def login(self, password):
        """Войти в систему."""
        if self.verify_password(password):
            self.last_login = datetime.now()
            return True
        return False
        
    def grant_access(self, user, resource):
        """Предоставить доступ."""
        return f"Доступ к {resource} предоставлен для {user}"
