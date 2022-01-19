# from collections import deque
#
#
# def solution(board):
#     check_move_board = [i[:] for i in board]
#
#     q = deque()
#     q.append([0, 0, 0, 1])
#     q.append([0, 1, 0, 0])
#
#     q_set = set()
#     q_set.add((0, 0))
#     q_set.add((0, 1))
#
#     time = 0
#
#     cir_ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
#     move_ds = ((0, 1, 0, 1), (1, 0, 1, 0), (0, -1, 0, -1), (-1, 0, -1, 0))
#
#     n = len(board)
#
#     while q:
#         a_x, a_y, b_x, b_y = q.popleft()
#
#         for d in move_ds:
#             a_dx = a_x + d[0]
#             a_dy = a_y + d[1]
#             b_dx = b_x + d[0]
#             b_dy = b_y + d[1]
#
#             if 0 <= a_dx < n and 0 <= a_dy < n and 0 <= b_dx < n and 0 <= b_dy < n:
#                 if (a_dx, a_dy) not in q_set and (b_dx, b_dy) not in q_set:
#                     if check_move_board[a_dx][a_dy] == 0:
#                         if check_move_board[a_dx][a_dy] == 0:
#                             check_move_board[a_dx][a_dy] = check_move_board[a_x][a_y] + 1
#                             # check_move_board[a_x][a_y] = check_move_board[a_x][a_y] + 1
#                             q.append([a_dx, a_dy, a_x, a_y])
#
#         for d in cir_ds:
#             a_dx = a_x + d[0]
#             a_dy = a_y + d[1]
#             b_dx = b_x + d[0]
#             b_dy = b_y + d[1]
#
#             if 0 <= a_dx < n and 0 <= a_dy < n and 0 <= b_dx < n and 0 <= b_dy < n:
#                 if (a_dx, a_dy) not in q_set and (b_dx, b_dy) not in q_set:
#                     if check_move_board[a_dx][a_dy] == 0:
#                         if check_move_board[a_dx][a_dy] == 0:
#                             check_move_board[a_dx][a_dy] = check_move_board[a_x][a_y] + 1
#                             # check_move_board[a_x][a_y] = check_move_board[a_x][a_y] + 1
#                             q.append([a_dx, a_dy, a_x, a_y])
#
#     print(*check_move_board, sep='\n')
#
#     return check_move_board[n - 1][n - 1] - 1
#
# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

# 주어진 조건대로 구현하다보니 코드가 난잡한 버전 / 속도는 빠름
# 대신, 코드 중복이 심함
# 이건 bfs가 아니라 구현이야

from collections import deque

# def solution(board):
#     # move_check_board = [i[:] for i in board]
#
#     n = len(board)
#
#     q = deque()
#     # 시작 위치, 비용
#     # (0, 0), (0, 1), 0
#     q.append((0, 0, 0, 1, 0))
#
#     total_pos = set()
#     total_pos.add((0, 0, 0, 1))
#
#     ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
#
#     while q:
#         l_x, l_y, r_x, r_y, cost = q.popleft()
#
#         # 이동
#         for d in ds:
#             next_l_x = l_x + d[0]
#             next_l_y = l_y + d[1]
#             next_r_x = r_x + d[0]
#             next_r_y = r_y + d[1]
#
#             if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
#                 if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
#                     if (next_l_x, next_l_y, next_r_x, next_r_y) not in total_pos:
#                         q.append((next_l_x, next_l_y, next_r_x, next_r_y, cost+1))
#                         total_pos.add((next_l_x, next_l_y, next_r_x, next_r_y))
#
#                         if (next_l_x == n-1 and next_l_y == n-1) or (next_r_x == n-1 and next_r_y == n-1):
#                             return cost+1
#
#         # 회전
#         for i in [-1, 1]:
#             # 가로 방향일때
#             next_l_x = l_x + i
#             next_l_y = l_y
#             next_r_x = r_x + i
#             next_r_y = r_y
#
#             if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
#                 if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
#                     if (l_x, l_y, l_x + i, l_y) not in total_pos:
#                         q.append((l_x, l_y, l_x + i, l_y, cost+1))
#                         total_pos.add((l_x, l_y, l_x + i, l_y))
#
#                         if (next_l_x == n-1 and next_l_y == n-1) or (next_r_x == n-1 and next_r_y == n-1):
#                             return cost+1
#
#                     if (r_x, r_y, r_x + i, r_y) not in total_pos:
#                         q.append((r_x, r_y, r_x + i, r_y, cost+1))
#                         total_pos.add((r_x, r_y, r_x + i, r_y))
#
#                         if (next_l_x == n-1 and next_l_y == n-1) or (next_r_x == n-1 and next_r_y == n-1):
#                             return cost+1
#
#             # 세로 방향일떄
#             next_l_x = l_x
#             next_l_y = l_y + i
#             next_r_x = r_x
#             next_r_y = r_y + i
#
#             if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
#                 if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
#                     if (l_x, l_y, l_x, l_y + i) not in total_pos:
#                         q.append((l_x, l_y, l_x, l_y + i, cost + 1))
#                         total_pos.add((l_x, l_y, l_x, l_y + i))
#
#                         if (next_l_x == n-1 and next_l_y == n-1) or (next_r_x == n-1 and next_r_y == n-1):
#                             return cost+1
#
#                     if (r_x, r_y, r_x, r_y + i) not in total_pos:
#                         q.append((r_x, r_y, r_x, r_y + i, cost + 1))
#                         total_pos.add((r_x, r_y, r_x, r_y + i))
#
#                         if (next_l_x == n-1 and next_l_y == n-1) or (next_r_x == n-1 and next_r_y == n-1):
#                             return cost+1

# 테스트 1 〉	통과 (0.13ms, 10.4MB)
# 테스트 2 〉	통과 (0.15ms, 10.3MB)
# 테스트 3 〉	통과 (0.13ms, 10.4MB)
# 테스트 4 〉	통과 (0.86ms, 10.3MB)
# 테스트 5 〉	통과 (0.45ms, 10.3MB)
# 테스트 6 〉	통과 (0.72ms, 10.4MB)
# 테스트 7 〉	통과 (1.93ms, 10.3MB)
# 테스트 8 〉	통과 (2.87ms, 10.4MB)
# 테스트 9 〉	통과 (2.91ms, 10.3MB)
# 테스트 10 〉	통과 (2.90ms, 10.3MB)
# 테스트 11 〉	통과 (1.78ms, 10.4MB)
# 테스트 12 〉	통과 (2.03ms, 10.3MB)
# 테스트 13 〉	통과 (60.59ms, 11.8MB)
# 테스트 14 〉	통과 (37.65ms, 11.1MB)

# 코드 중복은 줄였으나, 속도가 조금 느림

from collections import deque

def escape(l_x, l_y, r_x, r_y):
    global n

    if (l_x == n - 1 and l_y == n - 1) or (r_x == n - 1 and r_y == n - 1):
        return True
    else:
        return False

def put_new_element(q, total_pos, l_x, l_y, r_x, r_y, cost):
    q.append((l_x, l_y, r_x, r_y, cost))
    total_pos.add((l_x, l_y, r_x, r_y))

    return q, total_pos

def solution(board):
    # move_check_board = [i[:] for i in board]
    global n

    n = len(board)

    q = deque()
    # 시작 위치, 비용
    # (0, 0), (0, 1), 0
    q.append((0, 0, 0, 1, 0))

    total_pos = set()
    total_pos.add((0, 0, 0, 1))

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    while q:
        l_x, l_y, r_x, r_y, cost = q.popleft()

        if escape(l_x, l_y, r_x, r_y):
            return cost

        # 이동
        for d in ds:
            next_l_x = l_x + d[0]
            next_l_y = l_y + d[1]
            next_r_x = r_x + d[0]
            next_r_y = r_y + d[1]

            if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
                if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
                    if (next_l_x, next_l_y, next_r_x, next_r_y) not in total_pos:
                        q, total_pos = put_new_element(q=q,
                                                        total_pos=total_pos,
                                                        l_x=next_l_x,
                                                        l_y=next_l_y,
                                                        r_x=next_r_x,
                                                        r_y=next_r_y,
                                                        cost=cost+1)

        # 회전
        for i in [-1, 1]:
            # 가로 방향일때
            next_l_x = l_x + i
            next_l_y = l_y
            next_r_x = r_x + i
            next_r_y = r_y

            if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
                if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
                    if (l_x, l_y, l_x + i, l_y) not in total_pos:
                        q, total_pos = put_new_element(q=q,
                                                        total_pos=total_pos,
                                                        l_x=l_x,
                                                        l_y=l_y,
                                                        r_x=l_x + i,
                                                        r_y=l_y,
                                                        cost=cost+1)

                    if (r_x, r_y, r_x + i, r_y) not in total_pos:
                        q, total_pos = put_new_element(q=q,
                                                        total_pos=total_pos,
                                                        l_x=r_x,
                                                        l_y=r_y,
                                                        r_x=r_x + i,
                                                        r_y=r_y,
                                                        cost=cost+1)

            # 세로 방향일떄
            next_l_x = l_x
            next_l_y = l_y + i
            next_r_x = r_x
            next_r_y = r_y + i

            if 0 <= next_l_x < n and 0 <= next_l_y < n and 0 <= next_r_x < n and 0 <= next_r_y < n:
                if board[next_l_x][next_l_y] == 0 and board[next_r_x][next_r_y] == 0:
                    if (l_x, l_y, l_x, l_y + i) not in total_pos:
                        q, total_pos = put_new_element(q=q,
                                                        total_pos=total_pos,
                                                        l_x=l_x,
                                                        l_y=l_y,
                                                        r_x=l_x,
                                                        r_y=l_y + i,
                                                        cost=cost+1)

                    if (r_x, r_y, r_x, r_y + i) not in total_pos:
                        q, total_pos = put_new_element(q=q,
                                                        total_pos=total_pos,
                                                        l_x=r_x,
                                                        l_y=r_y,
                                                        r_x=r_x,
                                                        r_y=r_y + i,
                                                        cost=cost+1)

# 테스트 1 〉	통과 (0.16ms, 10.4MB)
# 테스트 2 〉	통과 (0.19ms, 10.3MB)
# 테스트 3 〉	통과 (0.18ms, 10.3MB)
# 테스트 4 〉	통과 (0.71ms, 10.3MB)
# 테스트 5 〉	통과 (0.57ms, 10.5MB)
# 테스트 6 〉	통과 (0.84ms, 10.1MB)
# 테스트 7 〉	통과 (2.30ms, 10.3MB)
# 테스트 8 〉	통과 (3.31ms, 10.2MB)
# 테스트 9 〉	통과 (3.49ms, 10.3MB)
# 테스트 10 〉	통과 (3.38ms, 10.4MB)
# 테스트 11 〉	통과 (1.84ms, 10.3MB)
# 테스트 12 〉	통과 (2.20ms, 10.4MB)
# 테스트 13 〉	통과 (67.55ms, 11.8MB)
# 테스트 14 〉	통과 (42.80ms, 11.4MB)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))