import timeit
from based_way import integrate
from threads import integrate_threaded
from processes import integrate_proc
from Cython_use import integrate as c_integrate

def square(x):
    return x**2


def time_integrate(f):
    time1 = timeit.timeit(lambda: f(square, 0, 10, n_iter=10**6), number = 3)
    time2 = timeit.timeit(lambda: f(square, 0, 10, n_iter=10**7), number = 3)
    time3 = timeit.timeit(lambda: f(square, 0, 10, n_iter=10**8), number = 3)
    return time1, time2, time3

def main():
    print("Базовый способ:", time_integrate(integrate))
    print("Потоки:", time_integrate(integrate_threaded))
    print("Процессы:", time_integrate(integrate_proc))
    print("Cython:", time_integrate(c_integrate))
    # NoGIL замеряется отдельно


if __name__ == "__main__":
    main()