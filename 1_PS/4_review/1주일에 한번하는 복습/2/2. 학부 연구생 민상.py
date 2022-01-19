def wind_move(x, y, visited, graph):
    global n, m

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    product = {1: (-1, 1, -1, 3),
               2: (0, -1, 2, -1),
               3: (3, 2, 1, 0),
               4: (1, 0, 3, 2)}

    for i in range(4):
        dx = x + ds[i][0]
        dy = y + ds[i][1]

        while 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] != 9:
                visited[dx][dy] = True
                if graph[dx][dy] != 0:
                    i = product[graph[dx][dy]][i]

                if i != -1:
                    dx += ds[i][0]
                    dy += ds[i][1]
                else:
                    break
            else:
                break

def check_place(visited):
    count = 0

    for v in visited:
        count += v.count(True)

    return count


if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    graph = []
    airconditions = []

    for i in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)

        for j in range(m):
            if temp[j] == 9:
                airconditions.append((i, j))

    visited = [[False] * m for i in range(n)]

    for aircondition in airconditions:
        x, y = aircondition
        visited[x][y] = True
        wind_move(x, y, visited, graph)

    print(check_place(visited))