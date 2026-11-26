import time
from functools import wraps


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Completed: {func.__name__}")
        return result

    return wrapper


def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper