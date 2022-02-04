"""
Date    : 2022.02.04
Update  : 2022.02.04
Source  : 1920.py
Purpose : set의 탐색 O(1)
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    for n in B:
        if n in A:
            print(1)
        else:
            print(0)