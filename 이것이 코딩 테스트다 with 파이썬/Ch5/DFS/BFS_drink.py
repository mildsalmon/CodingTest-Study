# n, m = map(int, input().split())
ice = []

checks = []
ice_count = 0
total_zero_count = 0
move_check = ((0, -1), (1, 0), (0, 1), (-1, 0))
start_point_y = 0
start_point_x = 0
start_point = -1
move_check_count = 0

n, m = 15, 14
z =['00000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111',]


for i in range(n):
    a = list(map(int, z[i]))

    ice.append(a[:])
    # check.append(a[:])

    for j in range(m):
        # print('a[j]', a[j])
        if a[j] == 0:
            total_zero_count = total_zero_count + 1

    if start_point == -1:
        try:
            start_point_y = a.index(0)
            print("start_point, start_point_y_1", start_point, start_point_y)
            start_point = 0
        except Exception as e:
            start_point == -1
            start_point_y = 0
        start_point_x = i
# print("zero_count", total_zero_count)
for k in range(n):
    start_point = -1
    checks.append([start_point_x, start_point_y])
    print("checks_1", checks)

    while checks:  # check in checks:
        dx = checks[-1][0]
        dy = checks[-1][1]
        ice[dx][dy] = 1
        print("checks_3", checks)
        move_check_count = 0
        print(*ice, sep='\n')
        for l in move_check:
            print("l", l)
            nx = dx + l[0]
            ny = dy + l[1]
            # print("nx,ny", nx,ny)
            # print("ice_2", ice[nx][ny])
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                print("nx,ny", nx, ny)
                print("ice", ice[nx][ny])
                if ice[nx][ny] == 0:
                    checks.append([nx, ny])
                    print("checks_2", checks)

                    print(*ice, sep='\n')
                    break
                else:
                    pass

            move_check_count = move_check_count + 1
            print("move_check_count", move_check_count)
        if move_check_count == 4:
            print("move_check_count", "4")
            checks.pop()

    if start_point == -1:
        try:
            start_point_y = ice[k].index(0)
        except Exception as e:
            start_point_y = 0
    start_point_x = k

    print("start_point_x, start_point_y_2", start_point_x, start_point_y)

    if ice[start_point_x][start_point_y] == 1:
        ice_count = ice_count + 1
        print("ice_count", ice_count)
    else:
        pass

print(ice_count)

