

class Coffee:
    def __init__(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not len(name) > 3:
            raise ValueError("Name must be at least 3 characters long")
        self.name = name
        
    #Returning a list of all orders for this coffee
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    #Returning a unique list of Customer instances who have ordered that coffee
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    # Total number of times this coffee has been ordered
    def num_orders(self):
        return len(self.orders())
    
    # Average price of this coffee based on its orders
    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders()) if len(self.orders()) > 0 else 0.0
        
        
