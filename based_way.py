import math
import timeit

# итерация 1
def integrate(f, a: float, b: float, *, n_iter=100000) -> float:
    """
    функция считает определенный интеграл функции f на отрезке [a, b]
    с помощью метода прямоугольников
    f - функция
    a - начало отрезка
    b - конец отрезка
    n_iter - количество разбиений отрезка
    возвращает приближенное значение интеграла

    >> integrate(math.cos, 0, math.pi, n_iter=1000)
    0.0031415926535898094

    >> integrate(lambda x: x**2 + 2*x + 1, 0, math.pi, n_iter=1000)
    23.321255039750636
    """

    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i*step) * step
    return acc


def time_integrate(f):
    time1 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**6), number = 3)
    time2 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**7), number = 3)
    time3 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**8), number = 3)
    return time1, time2, time3

#print(time_integrate(integrate))


