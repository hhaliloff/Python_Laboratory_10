from concurrent.futures import ThreadPoolExecutor
import math
import timeit

# итерация 2
def integrate_part(f, a: float, b: float, *, n_iter=100000) -> float:
    """
    функция считает определенный интеграл функции f на отрезке [a, b]
    с помощью метода прямоугольников
    f - функция
    a - начало отрезка
    b - конец отрезка
    n_iter - количество разбиений отрезка
    возвращает приближенное значение интеграла

    >>> integrate_part(math.cos, 0, math.pi, n_iter=1000)
    0.0031415926535898094

    >>> integrate_part(lambda x: x**2 + 2*x + 1, 0, math.pi, n_iter=1000)
    23.321255039750636
    """

    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i*step) * step
    return acc


def integrate_threaded(f, a: float, b: float, *, n_iter=100000, n_thread = 4) -> float:
    iter_per_thread = n_iter // n_thread
    chunk = (b-a) / n_thread
    final = 0
    future = []

    with ThreadPoolExecutor(max_workers=n_thread) as executor:
        for i in range(n_thread):
            a_i = a + i*chunk
            b_i = a_i + chunk

            future.append(executor.submit(integrate_part, f, a_i, b_i, n_iter=iter_per_thread))

        for f in future:
            final = final + f.result()

    return final



