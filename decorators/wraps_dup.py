from time import sleep
# from functools import wraps
# def do_twice(func):
#     @wraps(func)
#     def wrapper_do_twice(*args,**kwargs):
#          func(*args,**kwargs)
#          func(*args,**kwargs)
#     return wrapper_do_twice

# @do_twice
# def say_whee(name):
#      print(f"Hello! , {name}")

# print(say_whee.__name__)

# without wrapper

# def wraps_decorator_factory(original_func):
#     def decorator(wrapper_to_change):
#         wrapper_to_change.__name__=original_func.__name__
#         wrapper_to_change.__doc__=original_func.__doc__
#         return wrapper_to_change
#     return decorator

# def do_twice(func):
#     @wraps_decorator_factory(func)
#     def wrapper_do_twice(*args,**kwargs):
#          func(*args,**kwargs)
#          func(*args,**kwargs)
#     return wrapper_do_twice

# @do_twice
# def say(name):
#      print(f"Hello! , {name}")

# print(say.__name__)

# DONT CREATE A WRAPPER IF YOU DONT HAVE TO CHANGE ANY FUNCTIONALITY OF THE FUNCTION INSIDE.

def wraps_decorator_factory(original_func):
    def decorator(wrapper_to_change):
        def wrapper(*args, **kwargs):
            wrapper.__name__=original_func.__name__
            wrapper_to_change(*args, **kwargs)
        return wrapper
    return decorator

def do_twice(func):
    @wraps_decorator_factory(func)
    def wrapper_do_twice(*args,**kwargs):
         func(*args,**kwargs)
         func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def say_whee(name):
     print(f"Hello! , {name}")

print(say_whee.__name__) 