# 뱀

from collections import deque

n = int(input())
k = int(input())

# 기본 0
graph = [[0]*(n+1) for _ in range(n+1)]

# 사과 위치 1
apples = []

for _ in range(k):
    temp = list(map(int, input().split()))
    apples.append(temp)
    graph[temp[0]][temp[1]] = 1

l = int(input())
move = deque()

for _ in range(l):
    temp = list(input().split())
    move.append([int(temp[0]), temp[1]])

# 방향
ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
dn = 0

# 뱀 위치 2
head = [1, 1]
tail = deque()
tail.append(head)
graph[1][1] = 2

time = 0

move_s, move_d = move.popleft()

while True:
    now_x, now_y = head

    if time == move_s:
        if move_d == "D":
            dn += 1
        elif move_d == "L":
            dn -= 1
        dn %= 4
        if len(move) == 0:
            pass
        else:
            move_s, move_d = move.popleft()

    now_x += ds[dn][0]
    now_y += ds[dn][1]
    time += 1

    if 0 < now_x <= n and 0 < now_y <= n:
        if [now_x, now_y] not in tail:
            if graph[now_x][now_y] == 1:
                pass
            elif graph[now_x][now_y] == 0:
                tx, ty = tail.popleft()
                graph[tx][ty] = 0

            head = [now_x, now_y]
            tail.append([now_x, now_y])
            graph[now_x][now_y] = 2
        else:
            break
    else:
        break

print(time)

# 40분 / pass