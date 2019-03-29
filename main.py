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
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:

            if prime[p]:

                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        count_prime_numbers = 0
        for p in range(2, n):
            if prime[p]:
                print(p, )
                ++count_prime_numbers
    except TypeError:
        print("Please, insert positive integer number!")


if __name__ == '__main__':
    n = -1.123123
    print("Following are the prime numbers smaller than or equal to", n)

    (sieve_of_eratosthenes(n))
