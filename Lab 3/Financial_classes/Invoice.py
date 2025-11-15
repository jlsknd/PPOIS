class Invoice:
    """Класс счета."""
    
    def __init__(self, invoice_id, customer, amount, services):
        """
        Инициализация счета.
        
        Args:
            invoice_id: ID счета
            customer: Клиент
            amount: Сумма
            services: Список услуг
        """
        self.invoice_id = invoice_id
        self.customer = customer
        self.amount = amount
        self.services = services if isinstance(services, list) else [services]
        self.issue_date = datetime.now()
        self.due_date = None
        self.is_paid = False
        self.payment = None
        self.tax_rate = 0.2
        self.discount = 0
        
    def mark_as_paid(self, payment):
        """Отметить счет как оплаченный."""
        self.is_paid = True
        self.payment = payment
        
    def is_overdue(self):
        """Проверить просрочен ли счет."""
        if self.due_date and not self.is_paid:
            return datetime.now() > self.due_date
        return False
        
    def calculate_total(self):
        """Рассчитать общую сумму."""
        return self.amount
        
    def add_service(self, service):
        """Добавить услугу в счет."""
        self.services.append(service)

