# Ch4_구현_왕실의 나이트_문제

# 8x8 좌표 평면
# L자로만 이동할 수 있음, 좌표 평면 밖으로 못나감

# L자
# (2, 1), (2, -1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)
#
# 나이트 이동 경우의 수를 구하라
# 행 (1~8)
# 열 (a~h)

# Input
# 나이트 위치

# Output
# 나이트 이동 경우의 수

# 11분 25초

# y, x = list(input())
#
# nx = int(x)
# ny = ord(y) - ord('a') + 1
#
# ds = [(2, 1), (2, -1),
#       (-1, 2), (1, 2),
#       (-2, -1), (-2, 1),
#       (-1, -2), (1, -2)]
# count = 0
#
# for d in ds:
#     dx = nx + d[0]
#     dy = ny + d[1]
#
#     if dx < 1 or dx > 8 or dy < 1 or dy > 8:
#         continue
#     # print(dx, dy)
#     count = count + 1
#
# print(count)

# Ch4_구현_게임 개발_문제

# 맵 크기 NxM
# 육지 OR 바다
# 캐릭터 동서남북 중 하나 바라봄
# 맵 칸은 (A, B) => A -> N, M -> B
# A는 북쪽으로 떨어진 칸의 개수 = 행
# B는 서쪽으로 떨어진 칸의 개수 = 열

# 캐릭 움직임 메뉴얼
# 현재 방향에서 왼쪽 방향부터 갈 곳을 정함 (서 남 동 북)
# 왼쪽방향으로 회전하면서 가보지 않았으면 전진
# 네 방향 모두 가본 칸이거나 바다인 경우 바라보는 방향의 반대편으로 한칸 가고 반복 / 단 바다인 경우 움직임 멈춤

# Input
# N M (최대 50)
# A B d (방향)
    # 0 북 -> (-1, 0)
    # 1 동 -> (0, 1)
    # 2 남 -> (1, 0)
    # 3 서 -> (0, -1)
# 셋째줄부터 N 줄까지 맵 정보
    # 1 바다
    # 0 육지

n, m = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))
game_map = []
check_game_map = []

for i in range(n):
    row_map = list(map(int, input().split()))
    game_map.append(row_map)
    check_game_map.append(row_map)

ds = ((-1, 0),
      (0, 1),
      (1, 0),
      (0, -1))

count = 1

while True:
    check_game_map[a][b] = 1
    d_count = 0
    print("a, b", a, b)
    for i in range(len(ds)):
        d_count = d_count + 1
        dd = ds[d]
        d = (d - 1) % 4
        da = a + dd[0]
        db = b + dd[1]

        if da < 0 or da >= n or db < 0 or db >= m:
            continue
        else:
            if game_map[da][db] == 1 or check_game_map[da][db] == 1:
                if d_count == 4:
                    a = a - dd[0]
                    b = b - dd[1]
                    break
            else:
                a = da
                b = db
                count = count + 1
                break
    if game_map[a][b] == 1:
        break

print(count)

# -----------------

n, m = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))
game_map = []
check_game_map = []

for i in range(n):
    row_map = list(map(int, input().split()))
    game_map.append(row_map)
    check_game_map.append(row_map)

ds = ((-1, 0),
      (0, 1),
      (1, 0),
      (0, -1))

count = 1

while True:
    print("a, b", a, b)
    d_count = d_count + 1
    dd = ds[d]
    d = (d - 1) % 4
    da = a + dd[0]
    db = b + dd[1]

    if da < 0 or da >= n or db < 0 or db >= m:
        continue
    else:
        if game_map[da][db] == 1 or check_game_map[da][db] == 1:
            if d_count == 4:
                a = a - dd[0]
                b = b - dd[1]

        else:
            check_game_map[da][db] = 1
            d_count = 0
            a = da
            b = db
            count = count + 1

    if game_map[a][b] == 1:
        break

print(count)