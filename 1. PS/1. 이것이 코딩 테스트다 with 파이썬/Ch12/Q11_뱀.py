# 백준 3190번 문제

from collections import deque

n = int(input())

# 게임 맵
game_map = [[0] * (n+1) for _ in range(n+1)]

# 사과 관련
apple_count = int(input())
apple_pos = []
for i in range(apple_count):
    # apple_pos.append(list(map(int, input().split())))
    x, y = list(map(int, input().split()))
    game_map[x][y] = 2

# 뱀의 방향 회전 관련
snake_d_count = int(input())
# snake_d_info = deque()
snake_d_info = []
for i in range(snake_d_count):
    temp = list(input().split())
    # snake_d_info.append([int(temp[0]), temp[1]])
    snake_d_info.append([int(temp[0]), temp[1]])

# 뱀의 현재 방향
d = 0
# 뱀의 현재 방향에 따라 앞으로 갈 방향을 지정 (x - ds[d][0] 이런 식으로)
ds = [(0,1), (1,0), (0,-1), (-1,0)]

# 현재 뱀의 위치
pos = [1, 1]
# 뱀의 길이
snake_length = 1
# 게임 진행 시간
time = 0

# 머리 위치 저장하는 큐 // 생각해보니 머리는 스택으로 해도 될 듯
# 루프가 반복될 때마다 머리에 저장된 데이터가 추출됨.
# 머리는 시간이 지날때마다 다음 위치가 큐에 추가됨.
q_head_pos = deque()
q_head_pos.append(pos)

# 꼬리 위치를 저장하는 큐
# 다음 위치에 사과가 없으면 pop.
# 사과가 있으면 그냥 반복해서 꼬리 위치 보전
q_tail_pos = deque()
q_tail_pos.append(pos)

# 게임 시작시 뱀위 위치는 (맨위, 맨좌) = (1, 1)라서 map을 채우고 시작함.
game_map[pos[0]][pos[1]] = 1
# 방향 전환에 필요한 d를 가리키는 point
snake_d_info_point = 0

while True:
    x, y = q_head_pos.popleft()

    # 방향전환에 필요한 시간이 되면 방향 전환
    if len(snake_d_info) > snake_d_info_point:
        if time == snake_d_info[snake_d_info_point][0]:
            if snake_d_info[snake_d_info_point][1] == "D":
                d = (d + 1) % 4

            else:
                d = (d - 1) % 4
            # d_info_time, d_info_move = snake_d_info.popleft()
            snake_d_info_point += 1

    # 시간을 1초 증가시키고 다음 좌표를 탐색함.
    time += 1

    dx = x + ds[d][0]
    dy = y + ds[d][1]

    # 다음 좌표가 벽이거나 뱀의 몸통이면 게임 끝
    if dx < 1 or dx > n or dy < 1 or dy > n:
        break

    if game_map[dx][dy] == 1:
        break

    # 다음 좌표가 사과면 꼬리 유지, 사과가 아니면 꼬리 제거하고 맵 원상복구
    if game_map[dx][dy] != 2:
        tx, ty = q_tail_pos.popleft()
        game_map[tx][ty] = 0

    # 여기까지 왔으면, 장애물들은 다 통과한거니 맵을 채움.
    game_map[dx][dy] = 1

    # 다음 위치를 머리와 꼬리에 집어넣음.
    q_head_pos.append([dx, dy])
    q_tail_pos.append([dx, dy])

print(time)

# 1시간 45분 / Pass