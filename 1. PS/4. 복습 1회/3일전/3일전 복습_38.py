# 멀쩡한 사각형

from math import gcd


def solution(w, h):
    g = gcd(w, h)

    if g == 1:
        answer = w + h - 1
    elif g != 1:
        answer = (w // g + h // g - 1) * g
        print(answer)

    return (w * h) - answer

# 124 나라의 숫자

def solution(n):
    num = [1, 2, 4]
    answer = ''

    while n > 0:
        n -= 1
        answer = str(num[n % 3]) + answer
        n //= 3

    return answer