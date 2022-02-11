"""
Date    : 2022.02.11
Update  : 2022.02.11
Source  : 15961.py
Purpose : 투 포인터 / 슬라이딩 윈도우
url     : https://www.acmicpc.net/problem/15961
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys
from collections import deque

input = sys.stdin.readline


if __name__ == "__main__":
    n, d, k, c = list(map(int, input().split()))
    belts = [int(input()) for _ in range(n)] * 2

    eat = deque()
    count_array = [0 for _ in range(d+1)]
    count = 0
    max_eat = 0

    for i, belt in enumerate(belts):
        eat.append(belt)

        if count_array[belt] == 0:
            count += 1
        count_array[belt] += 1

        if i < k-1:
            continue

        if count_array[c] == 0:
            max_eat = max(max_eat, count+1)
        else:
            max_eat = max(max_eat, count)

        sushi = eat.popleft()

        if count_array[sushi] == 1:
            count -= 1
        count_array[sushi] -= 1

    print(max_eat)