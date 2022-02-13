"""
Date    : 2022.02.13
Update  : 2022.02.13
Source  : 18870.py
Purpose : 해시 / 정렬
url     : https://www.acmicpc.net/problem/18870
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    temp_array = sorted(set(array))
    num_by_index = dict()

    for i, value in enumerate(temp_array):
        num_by_index[value] = i

    for num in array:
        print(num_by_index[num], end=' ')