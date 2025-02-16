from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""
    def my_decorator(my_function: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time()
            try:
                result = my_function(*args, **kwargs)
                end_time = time()
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'Функция {my_function.__name__} завершила работу с результатом {result}\n')
                else:
                    print(f'Функция {my_function.__name__} завершила работу с результатом {result}')
                return result
            except Exception as e:
                end_time = time()
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'Функция {my_function.__name__} завершила работу с ошибкой {e} Inputs:{args},'
                                f'{kwargs}\n')
                else:
                    print(f'Функция {my_function.__name__} завершила работу с ошибкой {e} Inputs:{args}, {kwargs}')
        return wrapper
    return my_decorator


@log()
def division(x: int, y: int) -> float:
    return x / y


division(2, 1)
