from collections import deque

def search_minimum_distance(shark_pos, space):
    """
    상어가 모든 지점으로 가는 최단거리를 구함
    :param shark_pos: 상어 현재 위치
    :param space: 물고기 지도
    :return: 최단거리 지도
    """
    global n

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    x, y = shark_pos
    q = deque()
    q.append((x, y))
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] == -1 and space[dx][dy] <= shark_size:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append((dx, dy))

    return visited

def find_fish(minimum_distance_map):
    """
    상어가 먹을 수 있는 크기의 물고기를 찾는다.
    만약, 동일한 크기의 물고기가 존재한다면, 우선순위를 (1. 위, 2. 왼쪽)로 정하고 물고기를 찾는다.
    :param minimum_distance_map: 상어에서 모든 물고기까지 가는 최단거리 지도
    :return:
    """
    global n

    dist = 1e9
    fish_x = 0
    fish_y = 0

    for i in range(n):
        for j in range(n):
            if minimum_distance_map[i][j] != -1 and 0 < space[i][j] < shark_size:
                if minimum_distance_map[i][j] < dist:
                    dist = minimum_distance_map[i][j]
                    fish_x = i
                    fish_y = j

    if dist != 1e9:
        fish = [dist, fish_x, fish_y]
        return fish
    else:
        return None

def eat_shark(eat, size):
    """
    상어가 물고기를 먹는 메소드
    먹은 물고기 수가 상어 크기와 같다면, 상어 크기가 1 커진다.
    :param eat:
    :param size:
    :return:
    """
    eat += 1

    if eat == size:
        eat = 0
        size += 1

    return eat, size

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

    time = 0

    while True:
        space[shark_pos[0]][shark_pos[1]] = 0

        minimum_distance_map = search_minimum_distance(shark_pos, space)
        fish = find_fish(minimum_distance_map)

        if fish is not None:
            time += fish[0]
            shark_pos = (fish[1], fish[2])
            shark_eat, shark_size = eat_shark(shark_eat, shark_size)
        else:
            break

    print(time)