from collections import deque



if __name__ == "__main__":
    n = int(input())
    space = []
    shark_eat = 0
    shark_size = 2

    for i in range(n):
        temp = list(map(int, input().split()))
        space.append(temp)

        for j in range(n):
            if temp[j] == 9:
                shark_pos = (i, j)

                space[i][j] = 0

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))
    time = 0
    check = True
    while check:
        q = deque()
        q.append(shark_pos)
        visited = [[-1] * n for i in range(n)]
        visited[shark_pos[0]][shark_pos[1]] = 0

        while q:
            x, y = q.popleft()

            for d in ds:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    if visited[dx][dy] == -1 and space[dx][dy] <= shark_size:
                        visited[dx][dy] = visited[x][y] + 1
                        q.append((dx, dy))

        fish = [7, 0, 0, 0, 1e9]
        # print(visited)
        is_fish = False
        dist = 1e9
        for i in range(n):
            for j in range(n):
                if visited[i][j] != -1 and 0 < space[i][j] < shark_size:
                    if visited[i][j] < dist:
                        dist = visited[i][j]
                        fish = [i, j, dist]
                        is_fish = True

        if is_fish:
            time += fish[2]
            shark_pos = (fish[0], fish[1])
            space[shark_pos[0]][shark_pos[1]] = 0

            shark_eat += 1

            if shark_eat == shark_size:
                shark_eat = 0
                shark_size += 1
        else:
            break
        # print(time)
        # print(*space, sep='\n')
        # print()

    print(time)