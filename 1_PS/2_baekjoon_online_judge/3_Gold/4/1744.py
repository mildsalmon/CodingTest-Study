"""
Date    : 2022.02.09
Update  : 2022.02.09
Source  : 1744.py
Purpose : 그리디 / 정렬 / 분할 정복?
url     : https://www.acmicpc.net/problem/1744
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def make_max(array):
    temp = 0
    negative = 0

    if len(array) % 2 == 1:
        negative = array[-1]

    for i in range(len(array)//2):
        index = i*2

        if array[index] == 1 or array[index+1] == 1:
            temp += array[index] + array[index+1]
        else:
            temp += (array[index] * array[index+1])

    return temp, negative


if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]

    array.sort()
    positives = []
    negatives = []
    zeros = []

    for x in array:
        if x > 0:
            positives.append(x)
        elif x < 0:
            negatives.append(x)
        else:
            zeros.append(x)

    positives.reverse()
    result = 0

    negative_sum, negative = make_max(negatives)
    positive_sum, positive = make_max(positives)

    result = negative_sum + positive_sum

    if len(zeros) >= 1:
        result += positive
    elif len(zeros) == 0:
        result += positive + negative

    print(result)

