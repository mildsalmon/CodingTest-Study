"""
Date    : 2022.02.01
Update  : 2022.02.01
Source  : 2965.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/2965
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))

    diff_a_b = b - a - 1
    diff_c_b = c - b - 1

    print(max(diff_c_b, diff_a_b))