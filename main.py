import time


def benchmark(function):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = function(*args, **kwargs)
        print(function.__name__, time.time() - t)
        return res

    return wrapper


@benchmark
def sieve_of_eratosthenes(n):
    try:
        if n <= 0 or isinstance(n, float):
            raise TypeError("Please insert Integer value!")
        primes = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:

            if primes[p]:

                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        for p in range(2, n):
            if primes[p]:
                print(p, )
    except TypeError:
        print("Please, insert positive integer number!")


if __name__ == '__main__':
    n = 3
    print("Prime numbers before ", n, " are: ")

    (sieve_of_eratosthenes(n))
