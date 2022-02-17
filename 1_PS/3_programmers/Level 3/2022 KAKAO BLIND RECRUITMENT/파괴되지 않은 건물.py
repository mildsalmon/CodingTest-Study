"""
Date    : 2022.02.17
Update  : 2022.02.17
Source  : 파괴되지 않은 건물.py
Purpose : imos / 누적합 / 구현 / dp
url     : https://programmers.co.kr/learn/courses/30/lessons/92344
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(board, skill):
    count = 0
    imos = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skill:
        t, r1, c1, r2, c2, degree = s

        # 공격
        if t == 1:
            imos[r1][c1] -= degree
            imos[r1][c2 + 1] += degree
            imos[r2 + 1][c1] += degree
            imos[r2 + 1][c2 + 1] -= degree
        # 회복
        elif t == 2:
            imos[r1][c1] += degree
            imos[r1][c2 + 1] -= degree
            imos[r2 + 1][c1] -= degree
            imos[r2 + 1][c2 + 1] += degree

    for row in range(len(imos)):
        row_sum = 0

        for column in range(len(imos[0])):
            imos[row][column] += row_sum
            row_sum = imos[row][column]

    for column in range(len(imos[0])):
        column_sum = 0

        for row in range(len(imos)):
            imos[row][column] += column_sum
            column_sum = imos[row][column]

    for row in range(len(board)):
        for column in range(len(board[0])):
            board[row][column] += imos[row][column]

            if board[row][column] > 0:
                count += 1

    return count

# 채점을 시작합니다.
#
# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.07ms, 10.3MB)
# 테스트 3 〉	통과 (0.20ms, 10.3MB)
# 테스트 4 〉	통과 (0.40ms, 10.4MB)
# 테스트 5 〉	통과 (0.72ms, 10.3MB)
# 테스트 6 〉	통과 (1.11ms, 10.4MB)
# 테스트 7 〉	통과 (1.54ms, 10.4MB)
# 테스트 8 〉	통과 (2.15ms, 10.3MB)
# 테스트 9 〉	통과 (2.60ms, 10.4MB)
# 테스트 10 〉	통과 (4.13ms, 10.4MB)
#
# 효율성  테스트
#
# 테스트 1 〉	통과 (814.75ms, 143MB)
# 테스트 2 〉	통과 (997.79ms, 143MB)
# 테스트 3 〉	통과 (936.44ms, 143MB)
# 테스트 4 〉	통과 (809.51ms, 143MB)
# 테스트 5 〉	통과 (608.92ms, 132MB)
# 테스트 6 〉	통과 (625.43ms, 132MB)
# 테스트 7 〉	통과 (580.11ms, 132MB)
#
# 채점 결과
#
# 정확성: 53.8
# 효율성: 46.2
# 합계: 100.0 / 100.0