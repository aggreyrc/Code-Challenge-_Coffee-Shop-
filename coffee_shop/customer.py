from order import Order


class Customer:
    def __init__(self,name):
        
        # Validating name
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long")
        self.name = name
        
    # Returns a list of all orders for this customer.   
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]


    # Returns a unique list of coffees this customer has ordered.
    def coffees(self):
        return list({order.coffee for order in self.orders()})
        