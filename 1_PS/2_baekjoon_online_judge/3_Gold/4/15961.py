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
input = sys.stdin.readline


if __name__ == "__main__":
    n, d, k, c = list(map(int, input().split()))
    belts = [int(input()) for _ in range(n)]
    count_array = [0 for _ in range(d+1)]
    count_array[c] = 1e9
    count = 1

    for i in range(k):
        if count_array[belts[i]] == 0:
            count += 1
        count_array[belts[i]] += 1

    answer = count

    for i in range(k, n+k-1):
        if count_array[belts[i-k]] == 1:
            count -= 1
        count_array[belts[i-k]] -= 1

        if count_array[belts[i%n]] == 0:
            count += 1
        count_array[belts[i%n]] += 1

        answer = max(answer, count)

    print(answer)