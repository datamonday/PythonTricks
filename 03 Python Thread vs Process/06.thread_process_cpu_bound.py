import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

PRIMES = [314159265358973] * 1000


def is_prime(n):
    """
    判断是否为素数
    :param n: 输入数据
    :return: bool
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    """
    多线程
    :return:
    """
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    """
    多进程
    :return:
    """
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost:", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost:", end - start, "seconds")
