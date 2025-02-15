from time import time


def log(my_function, filename=None):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(start_time)
        try:
            print(f'Функция {my_function} завершили работу с результатом {my_function(*args, **kwargs)}')
        except Exception as e:
            print(f'Функция {my_function} завершили работу с ошибкой {e} Inputs:')
        end_time = time()
        print(end_time)
    return wrapper

@log
def division(x, y):
    return x / y

division(5,1)
