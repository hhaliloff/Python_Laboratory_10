import math
import timeit

# итерация 1
cpdef double integrate(f, double a, double b, n_iter=100000):
    """
    функция считает определенный интеграл функции f на отрезке [a, b]
    с помощью метода прямоугольников
    f - функция
    a - начало отрезка
    b - конец отрезка
    n_iter - количество разбиений отрезка
    возвращает приближенное значение интеграла

    >>> integrate(math.cos, 0, math.pi, n_iter=1000)
    0.0031415926535898094

    >>> integrate(lambda x: x**2 + 2*x + 1, 0, math.pi, n_iter=1000)
    23.321255039750636
    """

    cdef double acc = 0
    cdef double step = (b - a) / n_iter
    cdef int i
    for i in range(n_iter):
        acc = acc + f(a + i*step) * step
    return acc





