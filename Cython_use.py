from Cython import integrate
import timeit

def square(x):
    return x**2

def time_integrate(f):
    time1 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**6), number = 3)
    time2 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**7), number = 3)
    time3 = timeit.timeit(lambda: f(lambda x: x**2, 0, 10, n_iter=10**8), number = 3)
    return time1, time2, time3

print(time_integrate(integrate))