"""
Date    : 2021.12.09
Update  : 2021.12.09
Source  : Q46_아기 상어.py
Purpose : bfs를 이용하여 구현하는 문제인줄 알았는데.... 문제를 잘못이해해서 틀렸다.. 내 4시간..
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 물고기는 번호와 방향을 갖는다.
    # 방향을 45도 반시계로

# 초기

# 상어는 물고기를 먹고 물고기 방향으로 이동한다.
    # 물고기 먹고 빈칸 만들기

# 물고기도 움직임
    # 이동 x -> 상어가 있거나, 공간 밖
    # 번호가 작은 순서로 이동함.
    # 이동할 수 있을떄까지 45도 회전
    #이동 x면 이동 x
    # 다른 물고기칸으로 이동할떄는 서로 위치를 바꾸는 방식으로

# 물고기 이동 -> 상어 이동

# 상어
    # 방향에 있는 칸을 이동할 수 있고 한 번에 여러 칸을 이동할 수 있음
    # 물고기가 있는칸으로 이동하면, 물고기 먹고 물고기의 방향을 갖는다.
    # 지나가는 칸에 있는 물고기는 먹지 않음
    # 빈 칸으로는 이동하지 못함
        # 이동하던 중 칸이 없으면 집으로 돌아감 ==> 이거를 초기 시작위치인 0,0으로 돌아간다고 이해하고 풀었음

# 상어가 집으로 간 후에는 물고기가 다시 움직임 -> 반복
import copy

def fish_move(fishs):
    """
    물고기 이동 코드
    :param fishs:
    :return:
    """
    fish_moved = [False] * (n*n+1)

    for k in range(1, n * n + 1):
        for i in range(n):
            for j in range(n):
                if fishs[i][j][0] == k and not fish_moved[k]:
                    for dk in range(len(ds)):
                        next_pos = (fishs[i][j][1] + dk)%len(ds)
                        d = ds[next_pos]
                        dx = i + d[0]
                        dy = j + d[1]

                        if 0 <= dx < n and 0 <= dy < n:
                            if fishs[dx][dy][0] != 99:
                                fishs[i][j][1] = next_pos
                                fishs[i][j], fishs[dx][dy] = fishs[dx][dy], fishs[i][j]
                                fish_moved[k] = True
                                # print(*fishs, sep='\n')
                                # print()
                                break

def dfs(x, y, shark_eat, shark_direction, fishs):
    """
    상어 이동 코드드
   :param x:
    :param y:
    :param shark_eat:
    :param shark_direction:
    :param fishs:
    :return:
    """
    copy_fish = copy.deepcopy(fishs)
    shark_eat += copy_fish[x][y][0]
    copy_fish[x][y][0] = 99
    fish_move(copy_fish)
    eat_list = []
    shark_eat_list = []

    for i in range(1, n):
        next_pos = (shark_direction)
        d = ds[next_pos]
        dx = x + d[0] * i
        dy = y + d[1] * i

        if 0 <= dx < n and 0 <= dy < n:
            if copy_fish[dx][dy][0] != -1:
                eat_list.append((dx, dy))

    copy_fish[x][y][0] = -1

    if len(eat_list) == 0:
        return shark_eat

    for eat in eat_list:
        shark_direction = copy_fish[eat[0]][eat[1]][1]
        shark_eat_list.append(dfs(eat[0], eat[1], shark_eat, shark_direction, copy_fish))

    return max(shark_eat_list)


if __name__ == "__main__":
    n = 4

    fishs = []

    for i in range(n):
        temp = list(map(int, input().split()))

        fish = []
        for j in range(n):
            fish.append([temp[j*2], temp[j*2+1]-1])
        fishs.append(fish)

    ds = ((-1, 0), # 상
          (-1, -1), # 대 (왼상)
          (0, -1), # 왼
          (1, -1), # 대 (왼하)
          (1, 0), # 하
          (1, 1), # 대 (오하)
          (0, 1), # 오
          (-1, 1)) # 대 (오상)

    ds_len = len(ds)

    shark_pos = (0, 0)
    shark_direction = fishs[0][0][1]
    shark_eat = 0
    # shark_eat += fishs[0][0][0]

    shark_eat = dfs(shark_pos[0], shark_pos[1], shark_eat, shark_direction, fishs)

    # print(*fishs, sep='\n')
    print(shark_eat)