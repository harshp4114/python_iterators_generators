def decorator(func):
    print("deco is called")
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)

#  this is the plain vanilla way of writing decorators which is also a little clunky.
# First of all, you end up typing the name say_whee three times. Additionally, the 
# decoration gets hidden away below the definition of the function.

# using the pie syntax @

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        print(func)
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")


class CallCounter:
    def __init__(self, func):
        print("INIT Callled")
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
            print("__CALL__ called", self, args,kwargs,self.func)
            self.count += 1
            print(f"{self.func.__name__} has been called {self.count} times.")
            return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    print(f"Hello, {name}!")

class CallCounter:
    def __init__(self):
        print("INIT Callled")
        self.count = 0


obj=CallCounter()
def greet(name,obj):
    obj.count+=1
    print(f"Hello, {name}!")

#  decorating functions with arguments


def do_twice(func):
    print("establishing decorator")
    def wrapper_do_twice(*args,**kwargs):
            print("inside wrapper",args,kwargs,func,func.__name__) # here func.__name__ gives say_whee only but in the global scope it is changed to wrapper_do_twice
            # as say_whee is assigned with the wrapper returned from the decorator
        #   func(args,kwargs) this makes it compulsarily take 2 arguments
        #   func(args,kwargs)
            func(*args,**kwargs) # this allows any amount of arguments to be taken in the function
            func(*args,**kwargs)
    return wrapper_do_twice

# this calls the decorator as say_whee=do_twice(say_whee)
# by this, it will have the reference of the function say_whee in the func variable inside the wrapper function also
@do_twice
def say_whee(name):
     print(f"Hello! , {name}")

# to fix the above issue, we can use functools.wraps which will chnage the metadata of the wrapper with that of the function passed in the decorator @wraps(func)
from functools import wraps
def do_twice(func):
    @wraps(func)
    def wrapper_do_twice(*args,**kwargs):
         func(*args,**kwargs)
         func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def say_whee(name):
     print(f"Hello! , {name}")


# Returning Values From Decorated Functions

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam=return_greeting("Adam")
print(hi_adam) # this will return None as the return value from the func is eaten by the decorator.
                #this happens because it doesn't explicitly return the value of the func from the wrapper

# to solve this return the value from the last call of the func in the wrapper
def do_twice(func):
    @wraps(func)
    def wrapper_do_twice(*args,**kwargs):
         func(*args,**kwargs)
         return func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam=return_greeting("Adam")
print(hi_adam)