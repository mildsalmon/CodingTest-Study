# # Ch4_구현_왕실의 나이트
#
# # 8x8 좌표 평면
# # 나이트는 L자 형태로만 이동할 수 있고 정원 밖으로 나갈 수 없다.
# # 나이트는
#     # 1. 수평 2칸 이동 + 수직 1칸 이동
#     # 2. 수직 2칸 이동 + 수평 1칸 이동
# # 나이트가 이동할 수 있는 경우의 수를 출력하라
# # 행 위치를 1~8
# # 열 위치를 a~h
#
# # Input
#     # 나이트의 현재 위치(열행)
#
# # Output
#     # 나이트가 이동할 수 있는 경우의 수
#
# y, x = list(input())
#
# y = ord(y) - ord('a') + 1
# x = int(x)
#
# d = [(-2, -1), (-2, 1),
#      (2, -1), (2, 1),
#      (-1, -2), (1, -2),
#      (-1, 2), (1, 2)]
# count = 0
#
# for i in d:
#     dx = x + i[0]
#     dy = y + i[1]
#
#     if dx < 1 or dx > 8 or dy < 1 or dy > 8:
#         continue
#
#     count += 1
#
# print(count)
#
# # 11분 40초 / pass

# Ch4_구현_게임 개발

# NxM 직사각형 맵
# 육지 또는 바다
# 캐릭터는 동서남북 중 한 곳을 바라봄
# 맵의 칸은 (A, B) -> (행, 열)
# 캐릭터는 상하좌우 이동 / 바다 못감

# 캐릭터 메뉴얼
    # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
    # 캐릭터의 바로 왼쪽 방향에 가지 않은 칸이 있다면, 왼쪽 방향 전진,
        # 없다면 1단계
    # 네 방향이 모두 가본 칸이거나 바다인 경우 바라보는 방향을 유지한 채로 뒤로 한칸가고 1단계로 돌아감.
        # 이때 뒤쪽 방향이 바다이면 움직임을 멈춘다.

# Input
    # 맵의 세로 크기 N, 가로 크기 M
        # 3 <= N, M <= 50
    # 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d
        # d는 0 = 북
            # 1 = 동
            # 2 = 남
            # 3 = 서
    # 맵의 정보
        # 0 = 육지
        # 1 = 바다

# Output
    # 이동을 마친 후 캐릭터가 방문한 칸의 수

from collections import deque

n, m = list(map(int, input().split()))
A, B, d = list(map(int, input().split()))
game_map = []
check_map = [[0] * m for _ in range(n)]

for i in range(n):
    game_map.append(list(map(int, input().split())))

ds = [(-1, 0),
     (0, 1),
     (1, 0),
     (0, -1)]

q = deque()
q.append([A, B])
count = 0

while q:
    x, y = q.popleft()
    check_map[x][y] = 1
    count += 1
    sea_count = 0
    for i in range(4):
        d = (d - 1) % 4
        dx = x + ds[d][0]
        dy = y + ds[d][1]

        if sea_count == 4:
            x = x - ds[d][0]
            y = y - ds[d][1]
            if game_map[x][y] == 0:
                q.append([x, y])
                break

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue

        if game_map[dx][dy] == 1 or check_map[dx][dy] == 1:
            sea_count += 1
            continue

        q.append([dx, dy])
        break

    print(*check_map, sep='\n')
    print()

print(count)

# 30분 48초 / pass
