"""
Date    : 2022.02.13
Update  : 2022.02.13
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
    array = [int(input()) for _ in range(n)]

    counting_eat = [0 for _ in range(d+1)]
    counting_eat[c] = 1e9
    count = 1

    for i in range(k):
        if counting_eat[array[i]] == 0:
            count += 1
        counting_eat[array[i]] += 1

    answer = count

    for i in range(k, k + n - 1):
        if counting_eat[array[i-k]] == 1:
            count -= 1
        counting_eat[array[i-k]] -= 1

        if counting_eat[array[i%n]] == 0:
            count += 1
        counting_eat[array[i%n]] += 1

        answer = max(answer, count)

    print(answer)
