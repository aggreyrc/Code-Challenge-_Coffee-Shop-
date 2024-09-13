import pytest
from customer import Customer
from coffee import Coffee
from order import Order





def test_invalid_customer_name():
    # name too short
    with pytest.raises(ValueError):
        Customer("")

    # name too long
    with pytest.raises(ValueError):
        Customer("This is a very long name that should not be allowed")

    # name is not a string
    with pytest.raises(ValueError):
        Customer(9567)
        
def test_orders():
    customer = Customer("Aggrey")
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Mocha")
    
    customer.create_order(coffee1, 2.50)
    customer.create_order(coffee2, 3.00)
    
    orders = customer.orders()
    
    assert len(customer.orders()) == 2
    assert orders[0].coffee == coffee1
    assert orders[1].coffee == coffee2
    
def test_coffees():
    customer = Customer("Brian")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Mocha")
    
    customer.create_order(coffee1, 6.50)
    customer.create_order(coffee2, 4.00)
    
    coffees = customer.coffees()
    
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees
    
def test_create_order():
    customer = Customer("Jared")
    coffee = Coffee("Latte")
    price = 4.5
    
    new_order = customer.create_order(coffee, price)
    
    assert new_order.customer == customer
    assert new_order.coffee == coffee
    assert new_order.price == 4.5