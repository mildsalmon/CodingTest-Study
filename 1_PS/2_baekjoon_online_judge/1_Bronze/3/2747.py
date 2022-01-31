"""
Date    : 2022.01.31
Update  : 2022.01.31
Source  : 2747.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/2747
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    num1 = 0
    num2 = 1

    if n == 0:
        print(num1)
    if n == 1:
        print(num2)

    for i in range(2, n+1):
        num2 += num1
        num1 = num2 - num1

    print(num2)