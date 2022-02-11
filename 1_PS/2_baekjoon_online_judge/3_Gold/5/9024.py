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

        start = 0
        end = n-1
        sum_dict = dict()
        answer = 0
        mini = 1e9

        while start < end:
            num_sum = array[start] + array[end]

            if num_sum in sum_dict:
                sum_dict[num_sum] += 1
            elif num_sum not in sum_dict:
                sum_dict[num_sum] = 1

            mini = min(mini, abs(k - num_sum))

            if num_sum >= k:
                end -= 1
            elif num_sum < k:
                start += 1

        if mini == 0:
            answer = sum_dict[k]
        else:
            if k - mini in sum_dict:
                answer += sum_dict[k - mini]
            if k + mini in sum_dict:
                answer += sum_dict[k + mini]

        print(answer)



