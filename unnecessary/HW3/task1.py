import time

def cache_values(func):
    cached_values = dict()
    def wrapper(*args, **kwargs):
        if args[0] not in cached_values.keys():
            cached_values[args[0]] = func(*args, **kwargs)
        return cached_values[args[0]]
    return wrapper

@cache_values
def multiplier(number: int):
    return number * 2

for num in range(10):
    factorial(num)
