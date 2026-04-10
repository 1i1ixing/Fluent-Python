# Decorator simple example
def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
def target():
    print("running target")

print(target()) # now target = deco(target), which is the inner function returned by deco
print(target)

# Python EXECUTES decorator at the time of function definition, not at the time of function call. 
registry = []
def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()") 

## At this moment, if you import this module, you would see:
## running register(<function f1 at 0x000002387F587C40>)
## running register(<function f2 at 0x000002387F587D30>)
## If you call registry, you would also see f1 and f2 be registered

def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()

## at this moment, if you run this script, or try to use debug mode by putting a breakpoint before main(),
## you would first see f1 and f2 be registered, then you would see f1, f2, f3 be called in main()

# Closures
## A closure is a function with an extended scope that encompasses nonglobal variables "referenced" in the body of the function but not defined there.
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total # Because of the following issues, this is needed to tell Python that count and total are free variables in the closure of averager, not local variables in averager
        count += 1 # Python detects assignment in the body of the function, thus treats count as local variable, not a free variable in the closure of averager
        total += new_value # Python detects assignment in the body of the function, thus treats total as local variable, not a free variable in the closure of averager
        return total / count
    return averager

avg = make_averager()
print(avg(10)) # this will raise UnboundLocalError: local variable 'count' referenced before assignment

# Implementing a timer decorator
import time
def timer(func):
    def decorated_func(*args, **kwargs):
        start_time = time.time()
        # calling the func, thus Python could find the free variable func, which is the original factorial, 
        # but in the recursive body, when calling factorial, it is calling the decorated factorial,
        # that is why every recursive call is recorded in the timer 
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return decorated_func

@timer
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(4)) 
## here factorial = timer(factorial), which is the decorated_func
## when calling func in decorated_func, it is calling original factorial,
## however, at this moment, the recursive call to factorial in the body of original factorial is calling the decorated factorial

# Singledispatch decorator
## If you decorate a plain function with @singledispatch,
## it becomes a generic function: a group of functions to perform the same operation in
## different ways, depending on the type of the first argument
from functools import singledispatch
import html

@singledispatch   
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)   
def _(text):             
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)

print(htmlize(42)) # this will call the original htmlize, which is the generic function
print(htmlize('hello world')) # this will call the registered htmlize for str, which is the specialized function for str

# Parameterized decorator
registry = set()

def register(active=True):
    def decorate(func):   
        print('running register(active=%s)->decorate(%s)'% (active, func))
        if active:    
            registry.add(func)
        else:
            registry.discard(func)   
        return func   
    return decorate

## python executes the decorator function when define a function, thus here, calling register(active=False) to return the decorate function
## then use this decorate function to decorate f1, to generate a decorated f1
@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

print('registry ->', registry)

print(register()(f3)) # this is just calling register() to return decorate, and call decorate(f3)
print('registry ->', registry)
print(register(active=False)(f2))
print('registry ->', registry)






