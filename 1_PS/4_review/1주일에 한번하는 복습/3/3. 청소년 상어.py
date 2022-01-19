"""
Date    : 2022.01.01
Update  : 2022.01.01
Source  : 19236.py
Purpose : 구현
url     : https://www.acmicpc.net/problem/19236
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import copy

def fish_move(fishs):
    global n, ds

    visited = [False] * (n*n + 1)

    for fish_num in range(1, n*n+1):
        for x in range(n):
            for y in range(n):
                if fish_num == fishs[x][y][0] and not visited[fish_num]:
                    for dk in range(len(ds)):
                        d_num = (fishs[x][y][1] + dk)%len(ds)

                        dx = x + ds[d_num][0]
                        dy = y + ds[d_num][1]

                        # 다음 위치가 공간을 벗어나지 않거나,
                        if 0 <= dx < n and 0 <= dy < n:
                            # 다음 위치가 상어가 아닌 경우.
                            if fishs[dx][dy][0] != 99:
                                # 두 물고기 위치를 바꾼다.
                                fishs[x][y][1] = d_num
                                fishs[x][y], fishs[dx][dy] = fishs[dx][dy], fishs[x][y]
                                visited[fish_num] = True

                                break

def shark_dfs(fishs, shark_x, shark_y, shark_eat, shark_d):
    global n, ds, answer

    temp_fishs = copy.deepcopy(fishs)

    answer = max(answer, shark_eat)

    temp_fishs[shark_x][shark_y] = [99, shark_d]

    fish_move(temp_fishs)

    temp_fishs[shark_x][shark_y] = [-1, -1]

    for dk in range(1, n):
        dx = shark_x + ds[shark_d][0]*dk
        dy = shark_y + ds[shark_d][1]*dk

        if 0 <= dx < n and 0 <= dy < n:
            if temp_fishs[dx][dy][0] != -1:
                shark_dfs(temp_fishs, dx, dy, shark_eat + temp_fishs[dx][dy][0], temp_fishs[dx][dy][1])

    return False

if __name__ == "__main__":
    n = 4
    ds = ((-1, 0),
          (-1, -1),
          (0, -1),
          (1, -1),
          (1, 0),
          (1, 1),
          (0, 1),
          (-1, 1))

    fishs = [[] for _ in range(n)]

    answer = 0

    for i in range(n):
        row_fishs = list(map(int, input().split()))

        for j in range(n):
            col_fish = row_fishs[j*2:(j+1)*2]
            col_fish[1] -= 1
            fishs[i].append(col_fish)

    start_x, start_y = 0, 0
    # 상어 위치, 먹은 물고기, 방향
    # shark = [(start_x, start_y), fishs[start_x][start_y][0], fishs[start_x][start_y][1]]

    shark_dfs(fishs, start_x, start_y, fishs[start_x][start_y][0], fishs[start_x][start_y][1])

    print(answer)