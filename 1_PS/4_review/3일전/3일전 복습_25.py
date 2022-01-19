# Ch12_구현_뱀

from collections import deque

n = int(input())
k = int(input())

# 맵은 0으로 표시
game_map = [[0]*(n+1) for _ in range(n+1)]

# 사과는 2로 표시
for i in range(k):
    x, y = list(map(int, input().split()))
    game_map[x][y] = 2

l = int(input())
snake_distance = []

# 이것도 큐로 만들면 더 효율적일꺼 같음.
# 밑에 for문을 쓰지 않아도 되니까
for i in range(l):
    time, d = list(input().split())
    time = int(time)
    snake_distance.append((time, d))

# 뱀의 머리는 스택 / 굳이 스택이 아니여도 됨. 입력 -> 삭제를 반복하니까.
# 뱀의 꼬리는 큐
snake_head = [1, 1]
snake_tail = deque()

snake_tail.append((1, 1))

# 동남서북
# 처음 바라보는 방향이 오른쪽
# 오른쪽에서 오른쪽으로 방향을 바꾸면 남
#           왼쪽으로 방향을 바꾸면 북
distance = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake_d = 0
time = 0

# 게임은 종료조건을 만나기 전까지 끝나지 않음
while True:
    x, y = snake_head

    # 뱀의 방향은 게임 시작 시간으로부터 X초가 끝난 뒤에 회전한다.
    # 현재 시간과 뱀이 방향 바꾸는 시간을 비교하여 조건이 맞으면 방향을 바꿈
    for s in snake_distance:
        s_time, s_d = s
        if s_time == time:
            if s_d == "D":
                snake_d = (snake_d + 1) % 4
            elif s_d == "L":
                snake_d = (snake_d - 1) % 4

    # 시간을 추가함.
    # 현재 시간(Line 51 앞부분)이 0일때, dx 부분의 시간(Line 57 뒷부분)은 1임.
    time += 1

    # 다음 위치를 예상해본다.
    dx = x + distance[snake_d][0]
    dy = y + distance[snake_d][1]

    # 뱀이 벽에 부딪쳤을때
    if dx < 1 or dx > n or dy < 1 or dy > n:
        break
    # 뱀이 자기 몸과 부딪쳤을 때
    if game_map[dx][dy] == 1:
        break

    # 다음 위치에 사과가 없을 때
    if game_map[dx][dy] != 2:
        # 꼬리를 삭제하고 맵에서도 뱀의 꼬리 부분을 지운다.
        tx, ty = snake_tail.popleft()
        game_map[tx][ty] = 0
    # 다음 위치에 사과가 있을 때
    elif game_map[dx][dy] == 2:
        pass

    # 사과가 있든 없든, 다음 위치는 1(뱀)로 채움
    # 뱀의 머리(스택), 꼬리(큐)에도 다음 위치를 추가함.
    game_map[dx][dy] = 1
    snake_head = [dx, dy]
    snake_tail.append((dx, dy))

print(time)

# 43분 32초