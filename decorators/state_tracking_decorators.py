import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.count+=1
        return func(*args, **kwargs)
    wrapper_count_calls.count=0 # function attributes : metadata or data along with function
    return wrapper_count_calls

@count_calls
def greet():
    print("hello john")

greet()
greet()
print(greet.count)


# count calls as class decorator

class CountCalls:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        self.func=func
        self.count=0
    
    def __call__(self, *args, **kwargs):
        self.count+=1
        print(f"Call {self.count} of {self.func.__name__}()")
        return self.func(*args, **kwargs)
    
@CountCalls
def say_whee():
    print("Whee!")

say_whee()
