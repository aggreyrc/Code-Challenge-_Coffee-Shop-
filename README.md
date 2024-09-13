# Code-Challenge_Coffee-Shop

This is a project to using object-oriented programming principles, to create a Python application from scratch to model a Coffee Shop domain.

Scenario:

You are tasked with building a domain model for a Coffee Shop. Your model will consist of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

# Object Relationships Methods and Properties

- Order Class (`order.py`):
       - `customer` property returns the `Customer` instance for the order.
       - `coffee` property returns the `Coffee` instance for the order.
  - Coffee Class (`coffee.py`):
    - `orders()` method returns a list of all `Order` instances for that coffee.
    - `customers()` method returns a unique list of `Customer` instances who have ordered that coffee.
  - Customer Class (`customer.py`):
    - `orders()` method returns a list of all `Order` instances for that customer.
    - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

# Aggregate and Association Methods

 -Customer Class (`customer.py`):
     - `create_order(coffee, price)` method: Receives a `Coffee` instance and a price, creates a new `Order` instance, and associates it with that customer and the coffee.

- Coffee Class (`coffee.py`):
- `num_orders()` method: Returns the total number of times a coffee has been ordered.
- `average_price()` method: Returns the average price for a coffee based on its orders.
