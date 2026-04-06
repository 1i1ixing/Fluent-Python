# default dictionary: automatically initializes missing keys with a default value from a factory function
from collections import defaultdict
dd = defaultdict(list)
print(dd['key']) # prints [] instead of KeyError
dd['key'].append(1)
print(dd)

# __missing__ method: customize behavior for missing keys in a SUBCLASS of dict
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str): # if the key is already a string, but it is missing, raise error
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default='Cannot find key'):
        try:
            return self[key] # this get() method would delegate to __getitem__() to give the opportunity to __missing__ to act
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys() # check if the key or its string version is in the dictionary

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d[4]) # call dict.getitem, then call __missing__ 
print(d[1]) # call dict.getitem, then call __missing__ 
print(d.get(4)) # call StrKeyDict0.get, which calls dict.getitem, then call __missing__
print(d.get(1))
print(2 in d) # call StrKeyDict0.__contains__, which checks if '2' is in the keys
print(1 in d)

# Immutable Mapping: a read-only mapping type that cannot be modified after creation
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d) # create a read-only view of the dictionary
print(d_proxy[1]) # prints 'A'
print(d_proxy[2]) # raises KeyError because the key is missing
d[2] = 'B' # modify the original dictionary
print(d_proxy[2]) # prints 'B' because the proxy reflects changes to the original

# Key ordering depends on insertion order
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
d1 = dict(DIAL_CODES)
print(d1)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print(d2)
print('d2:', d2.keys())
print('d1 == d2:', d1 == d2) # True, because the order of keys does not matter in a dictionary