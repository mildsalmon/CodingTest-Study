# ch5_DFS/BFS_미로 탈출

from collections import deque

n, m = list(map(int, input().split()))
graph = []
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    graph.append(list(map(int, input())))

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in d:
        dx = x + i[0]
        dy = y + i[1]

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if graph[dx][dy] == 0:
            continue
        elif graph[dx][dy] == 1:
            graph[dx][dy] = graph[x][y] + 1
            q.append((dx, dy))
    if graph[n-1][m-1] != 1:
        break

print(graph[n-1][m-1])

# print(*graph, sep='\n')

# 21분 25초 / Pass