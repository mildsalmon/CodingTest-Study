from collections import deque

n, m = list(map(int, input().split()))

array = []

for i in range(n):
    temp = list(map(int, input()))

    array.append(temp)

q = deque()
q.append((0, 0))

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

while q:
    x, y = q.popleft()

    for d in ds:
        dx = x + d[0]
        dy = y + d[1]

        if 0 <= dx < n and 0 <= dy < m:
            if array[dx][dy] == 1:
                array[dx][dy] = array[x][y] + 1
                q.append((dx, dy))

print(array[n-1][m-1])