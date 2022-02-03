"""
Date    : 2022.02.03
Update  : 2022.02.03
Source  : 2579.py
Purpose :
url     : https://www.acmicpc.net/problem/2579
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stairs = []

    for _ in range(n):
        temp = int(input())
        stairs.append(temp)

    max_score = stairs[n-1]
    i = n-1
    sequence = False

    while True:
        if i == 0:
            break
        elif i == 1:
            if sequence:
                break
            else:
                max_score += stairs[i-1]
                break

        if sequence:
            max_score += stairs[i-2]
            i -= 2
            sequence = False
        else:
            if stairs[i-1] <= stairs[i-2]:
                max_score += stairs[i - 2]
                i -= 2
                sequence = False
            elif stairs[i-1] > stairs[i-2]:
                max_score += stairs[i-1]
                i -= 1
                sequence = True

    print(max_score)