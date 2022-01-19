"""
Date    : 2021.12.08
Update  : 2021.12.08
Source  : 16943.py
Purpose : A로 만들 수 있는 수 중 B보다 작은 가장 큰 수를 구하라.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import permutations

def check_len(A_len, B_len) -> bool:
    """
    불필요한 연산을 제외하기 위해서 완벽하게 불가능한 경우는 제외했다.
    A의 길이가 B보다 길다면. A 원소를 전부 사용하여 재배열할때, B보다 작은 수를 만드는 방법이 없다.
    :param A_len: A 문자열의 길이
    :param B_len: B 문자열의 길이
    :return:
    """
    if A_len > B_len:
        return False
    return True

def solution(A, B) -> int:
    """
    가능한 경우에 대해서만 판별을 진행했다.
    문자열의 시작이 0이라면, 문제의 조건에 따라 불가능하다.
    :param A: A 문자열
    :param B: B 문자열
    :return:
    """
    possible = check_len(len(A), len(B))
    answer = -1

    if possible:
        permu = list(permutations(A, len(A)))

        for p in permu:
            # 순열 리스트의 첫번째 원소가 0이 아닌 경우만 판단한다.
            if p[0] != '0':
                value = int(''.join(p))
                B = int(B)

                if value < B:
                    answer = max(value, answer)
                else:
                    continue

    return answer

if __name__ == "__main__":
    A, B = list(input().split())

    print(solution(A, B))

# 301 321
