n, m = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))

game_maps = []

for i in range(n):
    game_map = list(map(int, input().split()))

    game_maps.append(game_map)

d_map = [[0]*m for _ in range(n)]

direction = [(-1, 0),
             (0, 1),
             (1, 0),
             (0, -1)]

check_point = 0
count = 1

while True:
    d_map[a][b] = 1

    # 방향 전환
    d = (d-1) % len(direction)

    # 움직임
    na = a + direction[d][0]
    nb = b + direction[d][1]
    # print(na, nb)
    if game_maps[na][nb] == 0 and d_map[na][nb] == 0:
        a = na
        b = nb
        check_point = 0
        count = count + 1


    else:
        check_point = check_point + 1
    # print(check_point)
    if check_point == 4:
        na = a - direction[d][0]
        nb = b - direction[d][1]

        if game_maps[na][nb] == 1:
            break

        # if game_maps[na][nb] == 0:
        #     a = na
        #     b = nb
        #     check_point = 0
        # else:
        #     break

print(count)