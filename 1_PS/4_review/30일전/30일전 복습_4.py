# 음료수 얼려 먹기

from collections import deque

n, m = list(map(int, input().split()))

array = []

for i in range(n):
    array.append(list(map(int, input())))

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
count = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            count += 1
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for d in ds:
                    dx = x + d[0]
                    dy = y + d[1]

                    if 0 <= dx < n and 0 <= dy < m:
                        if array[dx][dy] == 0:
                            array[dx][dy] = 1
                            q.append((dx, dy))

print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111