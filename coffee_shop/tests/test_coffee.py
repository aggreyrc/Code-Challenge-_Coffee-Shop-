import pytest
from coffee import Coffee
from customer import Customer



def test_invalid_coffee_name():
    # Invalid name (too short)
    with pytest.raises(ValueError):
        Coffee("AB")
    
    # Invalid type (not a string)
    with pytest.raises(ValueError):
        Coffee(12345)
        
        
def test_num_orders():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    customer1.create_order(coffee, 3.0)
    customer2.create_order(coffee, 4.0)
    
    assert coffee.average_price() == 3.5

def test_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    
    customers = coffee.customers()
    
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers


