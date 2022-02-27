"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 10. 파괴되지 않은 건물.py
Purpose : imos / 누적합 / 구현 / dp
url     : https://programmers.co.kr/learn/courses/30/lessons/92344
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(board, skill):
    answer = 0
    temp_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skill:
        action, r1, c1, r2, c2, degree = s

        if action == 1:
            # 공격
            temp_board[r1][c1] -= degree
            temp_board[r1][c2 + 1] += degree
            temp_board[r2 + 1][c1] += degree
            temp_board[r2 + 1][c2 + 1] -= degree
        elif action == 2:
            # 회복
            temp_board[r1][c1] += degree
            temp_board[r1][c2 + 1] -= degree
            temp_board[r2 + 1][c1] -= degree
            temp_board[r2 + 1][c2 + 1] += degree

    for row in range(len(temp_board)):
        for col in range(1, len(temp_board[0])):
            temp_board[row][col] += temp_board[row][col - 1]

    for col in range(len(temp_board[0])):
        for row in range(1, len(temp_board)):
            temp_board[row][col] += temp_board[row - 1][col]

    for row in range(len(board)):
        for col in range(len(board[0])):
            if temp_board[row][col] + board[row][col] > 0:
                answer += 1

    return answer
