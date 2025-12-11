import functools


def repeat(_func=None, *, num_times=2):
    print("inside decorator factory",_func)
    def decorator_repeat(func):
        print("inside decorator",func)
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
    
# @repeat    
# def greet():
#     print("hello john")

# greet()


@repeat(num_times=6)    
def greet():
    print("hello john")

greet()