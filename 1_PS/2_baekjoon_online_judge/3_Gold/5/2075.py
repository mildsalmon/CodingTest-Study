"""
Date    : 2022.02.08
Update  : 2022.02.08
Source  : 2075.py
Purpose : 정렬 / extend/ 우선순위 큐(굳이?)
url     : https://www.acmicpc.net/problem/2075
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    array = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        array.extend(temp)

    array.sort()

    print(array[-n])