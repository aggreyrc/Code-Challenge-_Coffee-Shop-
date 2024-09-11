from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not len(name) > 3:
            raise ValueError("Name must be at least 3 characters long")
        self.name = name
        
    #Returning a list of all orders for this coffee
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]
    
    #Returning a unique list of Customer instances who have ordered that coffee
    def customers(self):
        return list({order.customer for order in self.orders()})
        