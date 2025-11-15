class GiftShop:
    """Класс сувенирного магазина."""
    
    def __init__(self):
        """Инициализация магазина."""
        self.inventory = {}
        self.sales = []
        self.revenue = 0.0
        
    def add_product(self, product, quantity):
        """Добавить товар."""
        if product.name in self.inventory:
            self.inventory[product.name]['quantity'] += quantity
        else:
            self.inventory[product.name] = {
                'product': product,
                'quantity': quantity
            }
            
    def sell_product(self, product_name, quantity, payment):
        """Продать товар."""
        if product_name in self.inventory:
            if self.inventory[product_name]['quantity'] >= quantity:
                self.inventory[product_name]['quantity'] -= quantity
                self.revenue += payment.amount
                self.sales.append({
                    'product': product_name,
                    'quantity': quantity,
                    'amount': payment.amount,
                    'timestamp': datetime.now()
                })
                return True
        return False
        
    def check_stock(self, product_name):
        """Проверить наличие."""
        if product_name in self.inventory:
            return self.inventory[product_name]['quantity']
        return 0
