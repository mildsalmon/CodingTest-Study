"""
Date    : 2022.02.13
Update  : 2022.02.13
Source  : 9024.py
Purpose : 정렬 / 이분 탐색 / 투 포인터
url     : https://www.acmicpc.net/problem/9024
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    for tc in range(int(input())):
        n, k = list(map(int, input().split()))
        array = list(map(int, input().split()))
        array.sort()

        start = 0
        end = n-1
        min_diff = 1e9
        count = 0

        while start != end:
            value = array[start] + array[end]

            if min_diff > abs(k - value):
                count = 1
                min_diff = abs(k - value)
            elif min_diff == abs(k - value):
                count += 1

            if value >= k:
                end -= 1
            elif value < k:
                start += 1

        print(count)