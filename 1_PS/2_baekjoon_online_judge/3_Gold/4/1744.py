"""
Date    : 2022.02.09
Update  : 2022.02.09
Source  : 1744.py
Purpose :
url     : https://www.acmicpc.net/problem/1744
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import combinations


def recursive(array, result):
    global max_num

    if len(array) <= 1:
        max_num = max(max_num, sum(array) + result)

        return

    for combi in combinations(array, 2):
        temp_result = result
        temp_result += combi[0] * combi[1]
        # diff_array = array.difference(combi)
        diff_array = array[:]
        diff_array.remove(combi[0])
        diff_array.remove(combi[1])

        recursive(diff_array, temp_result)
        temp_result += sum(diff_array)

        max_num = max(temp_result, max_num)


if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]

    max_num = sum(array)

    recursive(array, 0)

    print(max_num)
