# Treating a function like an object
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(5))
print(factorial.__doc__)
print(type(factorial))

# User-defined callable types
import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        '''Make the instance to behave like a function, i.e., to be callable'''
        return self.pick()
bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))

# Function Introspection
def greet(name):
    return f"Hello, {name}!"

print(greet.__dict__)  # View the function's attributes
greet.version = "1.0" # Add custom attributes to the function
greet.author = "Lixing" # Add custom attributes to the function
print(greet.__dict__)  # {'version': '1.0', 'author': 'Lixing', ...}
print(greet.version)  # "1.0" # Access the attribute

# From postional to keyword-only arguments
def tag(name, *content, cls=None, **attrs):
    '''
    name: first positional argument
    *content: any number of additional positional arguments, caputured in a tuple named content
    cls: an optional keyword-only argument with a default value of None
    **attrs: any number of keyword arguments, captured in a dict named attrs
    '''
    pass

def f(a, *, b):
    '''
    a is a positional argument
    b is a keyword-only argument
    The * enforces that all parameters following it must be passed as keyword arguments, not positional arguments.
    '''
    pass

# function annotations
def clip(text: str, max_len: int = 80) -> str:
    '''
    Python has no checks, enforcement, validation, or any other action is performed to annotations.
    '''
    return "Successfully clipped the text."

print(clip.__annotations__)