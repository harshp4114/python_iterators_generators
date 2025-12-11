import functools
import time

def slow_down(_func=None,*,rate=1):
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down
    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)

@slow_down(rate=3)
def for_loop(num):
    if num<1:
        return
    print(num)
    return for_loop(num-1)

for_loop(5)