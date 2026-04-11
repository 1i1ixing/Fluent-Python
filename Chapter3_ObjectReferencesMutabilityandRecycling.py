# Copies are shallow by default, thus only copy reference
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) # shallow copy of l1
l1.append(100)
l1[1].remove(55) 
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] # for mutable object, the operator += modifies the object in place
l2[2] += (10, 11) # for immutable object, the operator += creates a new object and rebinds the name to the new object
print('l1:', l1)
print('l2:', l2)

# Bad idea to have mutable types as parameters default
## Example
class HauntedBus:
    """A bus model haunted by ghost passengers"""
    def __init__(self, passengers=[]):
        # each default value is evaluated when the function is defined，
        # i.e., usually when the module is loaded，
        # and the default values become attributes of the function object.
        self.passengers = passengers   
    def pick(self, name):
        self.passengers.append(name)   
    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers) # ['Alice', 'Bill']
print(HauntedBus.__init__.__defaults__) # ([],) the default value of passengers is an empty list, which is shared by all instances of HauntedBus that use the default value
bus2 = HauntedBus()  
bus2.pick('Carrie')
print(bus2.passengers)
print(HauntedBus.__init__.__defaults__) # ([],) the default value of passengers is still an empty list, which is shared by bus2 and any other instance of HauntedBus that uses the default value
bus3 = HauntedBus()
print(bus3.passengers) # ['Carrie'] because bus3 also uses the default value, which is the same list as bus2's passengers

# Defensive programming with mutable parameters
## Think twice whether you want to change the original list passed into the caller
class HauntedBus:
    """A bus model haunted by ghost passengers"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers) # make a copy in order to avoid chaning the original list passed in by the caller
    def pick(self, name):
        self.passengers.append(name)   
    def drop(self, name):
        self.passengers.remove(name)

# Garbage Collection and Weak References
## The del statement deletes names, not objects. 
## An object may be garbage collected as result of a del command, 
## but only if the variable deleted holds the last reference to the object, or if the object becomes unreachable
## Weak references to an object do not increase its reference count
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)  
print(wref)
print(wref()) # {0, 1}
a_set = {2, 3, 4} 
print(wref()) # None, because the original set {0, 1} is garbage collected, thus the weak reference wref() returns None
## Please note that immutable objects like int and tuple often interned (shared) by Python's interpreter for efficiency. 
## They don't participate in the same reference counting and garbage collection cycles as mutable objects.

# Interning
## String literals and small integers are interned by Python, meaning that they are stored in a shared pool and reused to save memory.
## However, tuple literals are not interned by default, even if they contain only immutable objects.
s1 = "abc"
s2 = "abc"
print(s1 is s2) # True

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2) # False

int1 = 257
int2 = 257
print(int1 is int2) # False

int3 = -6
int4 = -6
print(int3 is int4) # True

tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(tup1 is tup2) # False，but Python only interns the empty tuple () by default
