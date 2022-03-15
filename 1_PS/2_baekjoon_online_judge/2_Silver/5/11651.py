"""
Date    : 2022.03.15
Update  : 2022.03.15
Source  : 11651.py
Purpose : 정렬 / functools.cmp_to_key
url     : https://www.acmicpc.net/problem/11651
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import functools


def cmp(n1, n2):
    if n1[1] > n2[1]:
        return 1
    elif n1[1] == n2[1]:
        if n1[0] > n2[0]:
            return 1
        elif n1[0] == n2[0]:
            return 0
        else:
            return -1
    else:
        return -1


if __name__ == "__main__":
    n = int(input())
    dots = [list(map(int, input().split())) for _ in range(n)]

    dots.sort(key=functools.cmp_to_key(cmp))

    for i in range(n):
        print(dots[i][0], dots[i][1])