"""
Date    : 2022.02.02
Update  : 2022.02.02
Source  : 1904.py
Purpose : 정렬 후 양쪽 끝에서 다가오는 투포인터 문제
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
        num2 += num1
        num1 = num2 - num1

    return num2


if __name__ == "__main__":
    n = int(input())

    print(tile(n))