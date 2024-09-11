from customer import Customer
from coffee import Coffee


class Order:
    def __init__(self,customer,coffee,price):
        if isinstance(customer,Customer) and isinstance(coffee,Coffee):
            self.customer = customer
            self.coffee = coffee
        else:
            raise ValueError("Customer and coffee must be instances of Customer and Coffee respectively")
        
        if not isinstance(price,float):
            raise ValueError("Price should be a Number with 1 decimal place")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price has to be between $1.0 and $10.0")
        self.price = price