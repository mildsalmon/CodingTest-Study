"""
Date    : 2022.02.10
Update  : 2022.02.10
Source  : 9024.py
Purpose : 투 포인터 / 이진탐색
url     : https://www.acmicpc.net/problem/9024
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    for tc in range(int(input())):
        n, k = list(map(int, input().split()))
        array = list(map(int, input().split()))

        array.sort()

        answer = 0
        mini = 1e9

        # 투포인터
        for i in range(n):
            start = i + 1
            end = n - 1

            # 이진탐색
            while start <= end:
                mid = (start + end) // 2
                sum_num = array[i] + array[mid]

                if abs(k - sum_num) < mini:
                    answer = 1
                    mini = abs(k - sum_num)
                elif abs(k - sum_num) == mini:
                    answer += 1

                if sum_num <= k:
                    start = mid + 1
                elif sum_num > k:
                    end = mid - 1

        print(answer)
