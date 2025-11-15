class Cafe:
    """Класс кафе в музее."""
    
    def __init__(self, name, capacity):
        """
        Инициализация кафе.
        
        Args:
            name: Название кафе
            capacity: Вместимость
        """
        self.name = name
        self.capacity = capacity
        self.menu = []
        self.orders = []
        self.current_customers = 0
        
    def add_menu_item(self, item):
        """Добавить позицию в меню."""
        self.menu.append(item)
        
    def place_order(self, customer, items):
        """Сделать заказ."""
        if self.current_customers >= self.capacity:
            raise CapacityExceededError("Кафе заполнено")
        order = {
            'customer': customer,
            'items': items,
            'timestamp': datetime.now()
        }
        self.orders.append(order)
        return order
        
    def serve_customer(self):
        """Обслужить клиента."""
        if self.current_customers < self.capacity:
            self.current_customers += 1
            
    def customer_leaves(self):
        """Клиент уходит."""
        if self.current_customers > 0:
            self.current_customers -= 1
