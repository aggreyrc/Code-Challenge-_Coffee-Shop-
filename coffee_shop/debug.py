from customer import Customer 
from coffee import Coffee
from order import Order

# creating a customer
customer = Customer("Kevin")
print(f"Customer created; {customer.name}")

# create coffees
coffee_1 = Coffee("Cappuccino")
coffee_2 = Coffee("Mocha")
print(f"Coffee created: {coffee_1.name}")
print(f"Coffee created: {coffee_2.name}")

# create orders
order_1 = Order(customer, coffee_1, 4.0)
order_2 = Order(customer, coffee_2, 5.0)
print(f"Order created:{order_1.customer.name} ordered {coffee_1.name} for ${order_1.price}")
print(f"Order created : {order_2.customer.name} ordered {coffee_2.name} for ${order_2.price}")

# Test the orders and coffees methods
print(f"{customer.name}'s orders: {[order.coffee.name for order in customer.orders()]}")


# Test coffee's orders and customers
print(f"Number of orders for {coffee_1.name}: {coffee_1.num_orders()}")
print(f"Average price for {coffee_1.name}: ${coffee_1.average_price():.2f}")
print(f"Customers who ordered {coffee_1.name}: {[customer.name for customer in coffee_1.customers()]}")
