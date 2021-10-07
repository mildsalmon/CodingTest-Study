from collections import deque

def bfs(temp_array, array, x, y):
    global n

    q = deque()
    q.append((x, y))

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    temp_array[x][y] = True
    save_country = [(x, y)]
    union_count = 1
    union_pop = array[x][y]

    while q:
        nx, ny = q.popleft()

        for d in ds:
            dx = nx + d[0]
            dy = ny + d[1]

            if 0 <= dx < n and 0 <= dy < n:
                diff = abs(array[nx][ny] - array[dx][dy])
                if l <= diff <= r:
                    if not temp_array[dx][dy]:
                        q.append((dx, dy))
                        temp_array[dx][dy] = True
                        save_country.append((dx, dy))
                        union_count += 1
                        union_pop += array[dx][dy]

    # if union_count != 1:
    for country in save_country:
        c_x, c_y = country

        array[c_x][c_y] = union_pop // union_count

    #     return True
    # else:
    #     return False


global n

n, l, r = list(map(int, input().split()))
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

count = 0

while True:
    temp_array = [[False]*n for i in range(n)]
    false_count = 0
    for i in range(n):
        for j in range(n):
            if not temp_array[i][j]:
                bfs(temp_array, array, i, j)
                false_count += 1

    if false_count == n*n:
        break
    else:
        count += 1

print(count)