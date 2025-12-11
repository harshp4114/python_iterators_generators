import functools 

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("count calls called",args)
        wrapper.num_call += 1
        print(f"function called {wrapper.num_call} times")
        return func(*args, **kwargs)
    wrapper.num_call = 0
    return wrapper

# this gives output as 177 times
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


#######################################################
def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("cache decorator called",args)
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache_keys:
            wrapper.cache_keys[cache_key] = func(*args, **kwargs)
        print("cache: ",wrapper.cache_keys)
        return wrapper.cache_keys[cache_key]
    wrapper.cache_keys = {}
    return wrapper

# this outputs function called 11 times
@count_calls
@cache
def fibonacci_cached(num):
    if num < 2:
        return num
    return fibonacci_cached(num-1) + fibonacci_cached(num-2)



# we did not understand why this function count of fibonacci_cached2 function is not equal to that of fibonacci function call 
# this outputs function called 19 times
# this is because in this count calls wrapper is first called before calling the cache wrapper, so it will count the function call even if the call isnt made to the functin
# to understand just trace the wrapper assignment in the heirarchy of decorators to the original function
@count_calls
@cache
def fibonacci_cached2(num):
    if num < 2:
        return num
    return fibonacci_cached2(num-1) + fibonacci_cached2(num-2)


fibonacci_cached(10)