"""
Date    : 2022.02.06
Update  : 2022.02.06
Source  : 2747.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/2747
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def fibo(n: int) -> int:
    if n <= 1:
        return n

    num1 = 0
    num2 = 1

    for _ in range(2, n+1):
        num2 += num1
        num1 = num2 - num1

    return num2

if __name__ == "__main__":
    n = int(input())

    print(fibo(n))