"""
Date    : 2022.02.07
Update  : 2022.02.07
Source  : 18870.py
Purpose : 정렬 / dict 인덱싱 O(1)
url     : https://www.acmicpc.net/problem/18870
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    arrays = list(map(int, input().split()))
    temp_array = sorted(set(arrays))

    for array in arrays:
        print(temp_array.index(array), end=' ')