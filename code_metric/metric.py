import time
from functools import wraps


def func_exec_time(func):
    """
    Decorator function reports the execution time
    """
    @wraps(func)  # 保留元信息
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} consume {end-start}s")
        return result
    return wrapper


