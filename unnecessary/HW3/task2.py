import time
from functools import wraps

def repeat_by_time(
    call_count: int,
    start_sleep_time: int,
    factor: int,
    border_sleep_time: int
    ):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Количество запусков = {call_count}\nНачало работы")
            for call_i in range(1, call_count + 1):
                t = start_sleep_time * factor**(call_i)
                t = border_sleep_time if t >= border_sleep_time else t
                time.sleep(t)
                func_result = func(*args, **kwargs)
                print(f"Запуск номер {call_i}. Ожидание: {t} секунд. Результат декорируемой функции = {func_result}")
        return wrapper
    return decorate


@repeat_by_time(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=15)
def multiplier(number: int):
    return number * 2

multiplier(24)
