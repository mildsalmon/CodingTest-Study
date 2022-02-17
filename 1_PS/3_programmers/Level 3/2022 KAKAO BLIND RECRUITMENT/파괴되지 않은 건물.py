"""
Date    : 2022.02.17
Update  : 2022.02.17
Source  : 파괴되지 않은 건물.py
Purpose : imos / 누적합 / 구현 / dp
url     : https://programmers.co.kr/learn/courses/30/lessons/92344
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def check_undestroy(board):
    count = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                count += 1

    return count


def solution(board, skill):
    for s in skill:
        t, r1, c1, r2, c2, degree = s

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if t == 1:
                    board[r][c] -= degree
                elif t == 2:
                    board[r][c] += degree

    return check_undestroy(board)

# 채점을 시작합니다.
#
# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.17ms, 9.94MB)
# 테스트 4 〉	통과 (0.60ms, 10.1MB)
# 테스트 5 〉	통과 (0.94ms, 10.2MB)
# 테스트 6 〉	통과 (1.89ms, 10.2MB)
# 테스트 7 〉	통과 (3.12ms, 10.2MB)
# 테스트 8 〉	통과 (4.77ms, 9.99MB)
# 테스트 9 〉	통과 (6.43ms, 10.3MB)
# 테스트 10 〉	통과 (13.10ms, 10.4MB)
#
# 효율성  테스트
#
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
#
# 채점 결과
#
# 정확성: 53.8
# 효율성: 0.0
# 합계: 53.8 / 100.0