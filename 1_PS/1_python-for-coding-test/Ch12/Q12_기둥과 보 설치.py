# def solution(n, build_frame):
#     game_map = [[5] * (n + 1) for _ in range(n + 1)]
#
#     for bf in build_frame:
#         x, y, a, b = bf
#         y = n - y
#         # game_map[y][x]
#         if b == 1:
#             # 설치
#             if a == 0:
#                 # 기둥
#                 if y == 5 or game_map[y][x] == 0 or game_map[y][x] == 1:
#                     game_map[y][x] = 0
#                     game_map[y - 1][x] = 0
#             elif a == 1:
#                 # 보
#                 if game_map[y][x] == 0 or game_map[y][x] == 1 or game_map[y][x - 1] == 1:
#                     game_map[y][x] = 1
#                     game_map[y][x + 1] = 1
#         elif b == 0:
#             # 삭제
#             if a == 0:
#                 # 기둥
#                 if game_map[y-1][x] != 0 or game_map[y-1][x] != 1:
#                     game_map[y][x] = 5
#                     # game_map[y - 1][x] = 5
#             elif a == 1:
#                 # 보
#                 if game_map[y][x+1] == 0 or (game_map[y][x-1] != 1 and game_map[y][x+1] != 1):
#                     game_map[y][x] = 5
#                     # game_map[y][x + 1] = 5
#
#     print(*game_map, sep='\n')
#     print()
#
#     answer = []
#
#     for row in range(n+1):
#         for column in range(n+1):
#             if game_map[column][5-row] != 5:
#                 # print(game_map[(n-row)][column])
#                 answer.append([column, 5-row, game_map[column][5-row]])
#
#     print(answer)
#
#     return b

def simulation(answers):
    for answer in answers:
        x, y, a = answer
        if a == 0:
            # 기둥
            if y != 0 or [x - 1, y, 1] not in answers or [x + 1, y, 1] not in answers or [x, y - 1, 0] not in answers:
                return False
        elif a == 1:
            # 보
            if [x, y - 1, 0] not in answers or [x + 1, y - 1, 0] not in answers or ([x - 1, y, 1] not in answers and [x + 1, y, 1] not in answers):
                return False
        return True


def solution(n, build_frame):
    answer = []

    for build in build_frame:
        x, y, a, b = build

        if b == 0:
            # 삭제
            answer.remove([x, y, a])
            simulation(answer)
            if simulation(answer) == False:
                # 시뮬레이션 결과 비정상
                answer.append([x, y, a])
        elif b == 1:
            # 설치
            answer.append([x, y, a])
            if simulation(answer) == False:
                # 시뮬레이션 결과 비정상
                answer.remove([x, y, a])
    answer.sort()
    return answer

# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])