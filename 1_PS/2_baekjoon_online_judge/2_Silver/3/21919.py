"""
Date    : 2022.2.28
Update  : 2022.2.28
Source  : 21919.py
Purpose :
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import math

def check_prime(array):
    primes = []

    for num in array:
        if is_prime(num):
            primes.append(num)

    return primes


def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def multiply(array):
    result = array[0]

    for num in array[1:]:
        result *= num

    return result


if __name__ == '__main__':
    n = int(input())
    array = set(map(int, input().split()))

    primes = check_prime(array)

    if len(primes):
        answer = multiply(primes)
        print(answer)
    else:
        print(-1)