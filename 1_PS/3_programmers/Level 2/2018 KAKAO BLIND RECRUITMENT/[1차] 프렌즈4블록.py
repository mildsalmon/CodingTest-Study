"""
Date    : 2022.04.13
Update  : 2022.04.13
Source  : [1차] 프렌즈4블록.py
Purpose : 전치행렬(transpose) / search / compression
url     : https://programmers.co.kr/learn/courses/30/lessons/17679
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def transpose(board):
    temp = [list(i)[::-1] for i in zip(*board)]

    return temp


def search(i, j, board, visited):
    ds = ((0, 0), (0, 1), (1, 0), (1, 1))

    blocks = [board[i + d[0]][j + d[1]] for d in ds]

    if blocks.count(blocks[0]) == 4:
        for d in ds:
            dx = i + d[0]
            dy = j + d[1]

            visited[dx][dy] = True
    else:
        return False


def count_break_block(visited):
    cnt = 0

    for i in range(len(visited)):
        cnt += visited[i].count(True)

    return cnt


def break_block(board, visited):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited[i][j]:
                board[i][j] = '.'

    for i in range(len(board)):
        cnt_break = board[i].count('.')

        if cnt_break != 0:
            for _ in range(cnt_break):
                board[i].pop(board[i].index('.'))
                board[i].append('#')


def solution(m, n, board):
    cnt = 0
    board = transpose(board)

    while True:
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != '#':
                    search(i, j, board, visited)

        temp = count_break_block(visited)

        if temp:
            cnt += temp
        else:
            break

        break_block(board, visited)

    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.3MB)
# 테스트 2 〉	통과 (0.10ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (1.39ms, 10.3MB)
# 테스트 5 〉	통과 (105.07ms, 10.3MB)
# 테스트 6 〉	통과 (8.07ms, 10.5MB)
# 테스트 7 〉	통과 (0.87ms, 10.5MB)
# 테스트 8 〉	통과 (1.44ms, 10.3MB)
# 테스트 9 〉	통과 (0.08ms, 10.5MB)
# 테스트 10 〉	통과 (0.90ms, 10.3MB)
# 테스트 11 〉	통과 (1.74ms, 10.3MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0