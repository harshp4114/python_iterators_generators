import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance=cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance=None
    return wrapper_singleton

@singleton
class Single:
    pass

first_one=Single()
second_one=Single()

print(id(first_one))
print(id(second_one))
print(first_one is second_one)