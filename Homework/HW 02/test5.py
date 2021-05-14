# 5. 用生成器的方式计算任意起止范围内质数的和。质数又称素数，是大于1的自然数，除了1和它本身外，不能被其他自然数整除。

from math import sqrt

# 判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    elif n >= 2:
        # 开平方，减少循环次数
        sqrt_n = int(sqrt(n))        
        for j in range(2, sqrt_n + 1):
            if n % j == 0:
                return False

        return True

# 生成器函数
def generator_prime(n):
    while True:
        if is_prime(n):
            yield n
            
        n += 1

# 对指定区间内的素数求和
def sum_of_prime_by_iter(start, end):
    sum_prime = 0
    list_prime = []
    
    for number in generator_prime(start):
        # 生成器不会停止，所以需要添加循环终止条件
        if number <= end:
            sum_prime += number
            list_prime.append(number)
        else:
            return sum_prime, list_prime
            
            
sum_prime, list_prime = sum_of_prime_by_iter(2, 101)
print("sum:  ", sum_prime)
print("prime:", list_prime)

"""
sum:   1161
prime: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
"""

