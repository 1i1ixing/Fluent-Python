# Generator: enclosed in parentheses, same syntax as listcomps
symbols = '$¢£¥€¤'
gen = (ord(symbols) for symbols in symbols) #gen is a generator
print(tuple(gen)) #tuples can be built from generators

# Named Tuples: subclass of tuples with named fields
from collections import namedtuple
CityConstuct = namedtuple('City', 'name country population coordinates') # CityConstuct is referring to the City subclass defined in namedtuple factory function
tokyo = CityConstuct('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) # create an instance of City
print(tokyo)
print(CityConstuct._fields) # return the field names

LatLongConstuct = namedtuple('LatLong', 'lat long')
shanghai_data = ('Shanghai', 'CN', 17.836, LatLongConstuct(31.166667, 121.466667))
shanghai = CityConstuct._make(shanghai_data) #make an instance of City from a sequence or iterable，_make is a class method
print(shanghai)
print(shanghai._asdict()) # return a new OrderedDict which maps field names to their values, _asdict is an instance method

# Slicing: in a * n, if a is a sequence containing MUTABLE objects, it will create a sequence that all the positions referring to the same mutable object
lst = [[]] * 3
lst[0].append('X')
print(lst)

lst = [['O'] * 3] * 3
lst[0].append('X')
print(lst) 

lst = [['O'] * 3 for i in range(3)]
lst[0].append('X') 
print(lst)

# Augumented Assignment:
a = [1,2]
b = [3,4]
print(id(a))
a += b # inplace assignment
print(id(a)) # same address

a = [1,2]
b = [3,4]
print(id(a))
a = a + b # a + b creates a new list and rebounds to a
print(id(a)) # different address

t = (1, 2, [10,30])
print(id(t[2]))
t[2] += [40,50]
print(t) # it would output error, but it works
print(id(t[2])) # same address

t = (1, 2, [10,30])
print(id(t[2]))
t[2] = t[2] + [40,50]
print(t) # it would output error, but it doesn't work
print(id(t[2])) # same address