# Simplify design patterns with first-order functions
## Design Patterns are reusable solutions to common software design problems. They provide a way to structure code in a way that is maintainable, flexible, and scalable.
## Design patterns could be separated into Strategy, Command, Template Method and Visitor, which could be simplified with first-order functions.
## Strategy Pattern Case
### Classic Strategy Pattern
from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity
    
class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
        def due(self):
            if self.promotion is None:
                discount = 0
            else:
                discount = self.promotion.discount(self) # self is Order instance, which is needed in Promotion.discount()
            return self.total() - discount
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
    
class Promotion(ABC):  # the Strategy: an abstract base class
    '''
    An abstract method is a method that is declared but has no implementation, and must be implemented by any subclass.
    Every concrete subclass must implement all abstract methods
    Otherwise, that subclass is still considered abstract and cannot be instantiated
    '''
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0
    
class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

### Using First-Order Functions to simplify Strategy Pattern
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity
    
class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self) # now self.promotion is a function, which takes self, which is an Order instance
        return self.total() - discount
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
    
def fidelity_promo(order): # It is now a function, which needs an Order instance 
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order): # It is now a function, which needs an Order instance 
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order): # It is now a function, which needs an Order instance 
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0