


class Customer:
    def __init__(self,name):
        
        # Validating name
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long")
        self.name = name
        self._order = []
        
    # Returns a list of all orders for this customer.   
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
       


    # Returns a unique list of coffees this customer has ordered.
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    # New order for this customer 
    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        if not isinstance(price, float):
            raise ValueError("Price must be a Number with 1 decimal place")
        
        new_order = Order(self, coffee, price)
        return new_order

