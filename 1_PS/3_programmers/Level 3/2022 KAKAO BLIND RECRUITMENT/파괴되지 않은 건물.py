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
        for column in range(1, len(imos[0])):
            imos[row][column] += imos[row][column - 1]

    for column in range(len(imos[0])):
        for row in range(1, len(imos)):
            imos[row][column] += imos[row - 1][column]

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
# 테스트 1 〉	통과(0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.5MB)
# 테스트 3 〉	통과 (0.20ms, 10.3MB)
# 테스트 4 〉	통과 (0.42ms, 10.2MB)
# 테스트 5 〉	통과 (1.31ms, 10.4MB)
# 테스트 6 〉	통과 (1.08ms, 10.3MB)
# 테스트 7 〉	통과 (1.58ms, 10.2MB)
# 테스트 8 〉	통과 (2.05ms, 10.5MB)
# 테스트 9 〉	통과 (2.65ms, 10.3MB)
# 테스트 10 〉	통과 (4.54ms, 10.4MB)
#
# 효율성  테스트
#
# 테스트 1 〉	통과 (952.45ms, 143MB)
# 테스트 2 〉	통과 (978.83ms, 143MB)
# 테스트 3 〉	통과 (948.02ms, 143MB)
# 테스트 4 〉	통과 (1019.89ms, 143MB)
# 테스트 5 〉	통과 (582.06ms, 132MB)
# 테스트 6 〉	통과 (606.55ms, 132MB)
# 테스트 7 〉	통과 (658.22ms, 132MB)
#
# 채점 결과
#
# 정확성: 53.8
# 효율성: 46.2
# 합계: 100.0 / 100.0