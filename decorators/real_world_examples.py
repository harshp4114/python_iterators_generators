# timer decorator
from functools import wraps
import time

# print("above deco")
# def timer(func):
#     print("decorator intialised")
#     @wraps(func)
#     def wrapper_timer(*args,**kwargs):
#         start_time=time.perf_counter()
#         val=func(*args,**kwargs)
#         end_time=time.perf_counter()
#         run_time=end_time-start_time
#         print(f"Finished {func.__name__}() in {run_time:.4f} secs")
#         return val
#     return wrapper_timer

# print("before deco")
# @timer
# def waste_some_time():
#     print("timer started")
#     time.sleep(4)
#     print("timer ended")

# print("after deco")


# debug decorator
# def debug(func):
    #   @wraps(func)
#     def wrapper_debug(*args,**kwargs):
#         args_l=[repr(a) for a in args]
#         kwargs_l=[f"{k}={repr(kwargs[k])}" for k in kwargs]
#         signature=', '.join(args_l+kwargs_l)
#         print(f"Calling {func.__name__}({signature})")
#         val=func(*args,**kwargs)
#         print(f"{func.__name__}() returned {repr(val)}")
#         return val
#     return wrapper_debug

# @debug
# def add(*args,**kwargs):
#     val=sum(args)
#     return val

# slow down decorator
def slow_down(func):
    @wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(4)
        val=func(*args, **kwargs)
        return val
    return wrapper_slow_down

@slow_down
def countdown(num):
    if num<1:
        print("Liftoff!")
    else:
        print(num)
        countdown(num-1)