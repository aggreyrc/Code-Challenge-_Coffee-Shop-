import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def test_price_not_a_float():
    customer = Customer("Bob")
    coffee = Coffee("Cappuccino")

    # Price not a float
    with pytest.raises(ValueError):
        Order(customer, coffee, "ten dollars")  # invalid string input


def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_invalid_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    
    # Price out of range
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

    # Price not a float
    with pytest.raises(ValueError):
        Order(customer, coffee, "invalid")

    # Price below range
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

