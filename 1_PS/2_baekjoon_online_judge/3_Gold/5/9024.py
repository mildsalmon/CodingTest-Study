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

        while start != end:
            num_sum = array[start] + array[end]

            if num_sum in sum_dict:
                sum_dict[num_sum] += 1
            elif num_sum not in sum_dict:
                sum_dict[num_sum] = 1

            # if num_sum == k:
            #     start += 1
            #     end -= 1
            if num_sum >= k:
                end -= 1
            elif num_sum < k:
                start += 1

        num_sums = sorted(sum_dict.keys())

        for i in range(k):
            if i == 0 and k in sum_dict:
                answer += sum_dict[k]
                break
            if k-i in sum_dict:
                answer += sum_dict[k-i]
            if k+i in sum_dict:
                answer += sum_dict[k+i]

            if answer != 0:
                break
            # if i == 0 and binary_search(k):
            #     answer += sum_dict[k]
            #     break
            #
            # elif k-i in sum_dict:
            #
            #
            # elif binary_search(k-i) or binary_search(k+i):
            #     answer += sum_dict[k-i]
            #     answer += sum_dict[k+i]
            #     break
        print(answer)


