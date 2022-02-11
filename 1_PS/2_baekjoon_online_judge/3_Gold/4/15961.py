"""
Date    : 2022.02.11
Update  : 2022.02.11
Source  : 15961.py
Purpose : 투 포인터 /
url     : https://www.acmicpc.net/problem/15961
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, d, k, c = list(map(int, input().split()))
    belts = [int(input()) for _ in range(n)] * 2
    eat_max = 0

    belts_set = set(belts)

    coupon_sushi = False

    if c in belts_set:
        coupon_sushi = True

    for start in range(n):
        count = 1
        ###
        for end in range(start, start + k - 1):
            if belts[end+1] in belts[start:end+1]:
                break
            count += 1
            end += 1

        if c not in belts[start:end+1]:
            if coupon_sushi:
                if c == belts[start-1] or c == belts[end+1]:
                    count += 1
            elif not coupon_sushi:
                count += 1

        eat_max = max(eat_max, count)

    print(eat_max)