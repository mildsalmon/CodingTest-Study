"""
Date    : 2022.02.02
Update  : 2022.02.02
Source  : 1904.py
Purpose : DP
url     : https://www.acmicpc.net/problem/1904
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def tile(n):
    num1 = 1
    num2 = 2

    if n == 1:
        return num1
    elif n == 2:
        return num2

    for i in range(3, n+1):
        num1, num2 = num2, (num1 + num2) % 15746

    return num2


if __name__ == "__main__":
    n = int(input())

    print(tile(n))