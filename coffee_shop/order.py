
class Order:
    
    all_orders = []
    def __init__(self,customer,coffee,price):
        
        #Validating class instances and attributes
        from customer import Customer
        from coffee import Coffee
        if isinstance(customer,Customer) and isinstance(coffee,Coffee):
            self._customer = customer
            self._coffee = coffee
        else:
            raise ValueError("Customer and coffee must be instances of Customer and Coffee respectively")
        
        if not isinstance(price,float):
            raise ValueError("Price should be a Number with 1 decimal place")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price has to be between $1.0 and $10.0")
        self.price = price
        
        Order.all_orders.append(self)
        
        
    #Returning Customer and Coffee instances for the order
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    
