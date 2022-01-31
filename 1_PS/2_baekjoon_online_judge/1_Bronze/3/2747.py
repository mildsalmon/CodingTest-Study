"""
Date    : 2022.01.31
Update  : 2022.01.31
Source  : 2747.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/2747
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def fibo(n):
    num1 = 0
    num2 = 1

    if n == 0:
        return num1
    if n == 1:
        return num2

    for i in range(2, n+1):
        num2 += num1
        num1 = num2 - num1

    return num2

if __name__ == "__main__":
    n = int(input())

    print(fibo(n))