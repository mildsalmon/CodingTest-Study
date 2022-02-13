"""
Date    : 2022.02.13
Update  : 2022.02.13
Source  : 1744.py
Purpose : 정렬
url     : https://www.acmicpc.net/problem/1744
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def sum_multiple(array):
    remain_value = 0
    value = 0

    if len(array) % 2 == 1:
        remain_value = array[-1]

    for i in range(1, len(array), 2):
        A, B = array[i-1], array[i]
        value += max(A * B, A + B)

    return [value, remain_value]


if __name__ == "__main__":
    n = int(input())
    negatives = []
    positives = []
    zeros = []
    answer = 0

    for _ in range(n):
        temp = int(input())

        if temp > 0:
            positives.append(temp)
        elif temp < 0:
            negatives.append(temp)
        else:
            zeros.append(temp)

    positives.sort(reverse=True)
    negatives.sort()

    value, negative = sum_multiple(negatives)
    answer += value
    value, positive = sum_multiple(positives)
    answer += value

    if zeros:
        answer += positive
    else:
        answer += positive + negative

    print(answer)