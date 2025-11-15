class Container:
    """Класс контейнера."""
    
    def __init__(self, container_id, container_type, max_weight):
        """
        Инициализация контейнера.
        
        Args:
            container_id: ID контейнера
            container_type: Тип (20ft, 40ft)
            max_weight: Максимальный вес
        """
        self.container_id = container_id
        self.container_type = container_type
        self.max_weight = max_weight
        self.current_weight = 0
        self.is_sealed = False
        self.contents = []
        self.seal_number = None
        self.customs_cleared = False
        self.owner = None
        
    def add_cargo(self, cargo_item):
        """Добавить груз в контейнер."""
        if self.is_sealed:
            raise VehicleUnavailableError("Контейнер опечатан")
        if self.current_weight + cargo_item['weight'] > self.max_weight:
            raise OverweightError("Превышен максимальный вес контейнера")
        self.contents.append(cargo_item)
        self.current_weight += cargo_item['weight']
        
    def seal_container(self):
        """Опечатать контейнер."""
        self.is_sealed = True
        
    def unseal_container(self):
        """Распечатать контейнер."""
        self.is_sealed = False
        
    def get_contents_list(self):
        """Получить список содержимого."""
        return self.contents
