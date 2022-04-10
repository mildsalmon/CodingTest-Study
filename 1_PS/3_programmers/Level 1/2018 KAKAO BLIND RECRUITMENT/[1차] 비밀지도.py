"""
Date    : 2022.04.11
Update  : 2022.04.11
Source  : [1차] 비밀지도.py
Purpose : 2진수 / 구현
url     : https://programmers.co.kr/learn/courses/30/lessons/17681
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def convert_binary(result, arr, n):
    for num in arr:
        binary = format(num, '0b')

        if len(binary) < n:
            binary = '0' * (n - len(binary)) + binary

        result.append(binary)


def concat_map(arr1, arr2, n):
    answer = []

    for a, b in zip(arr1, arr2):
        temp = ''
        # test
        for i in range(n):
            if a[i] == '0' and b[i] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)

    return answer


def solution(n, arr1, arr2):
    arr1_bi = []
    arr2_bi = []

    convert_binary(arr1_bi, arr1, n)
    convert_binary(arr2_bi, arr2, n)

    answer = concat_map(arr1_bi, arr2_bi, n)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0