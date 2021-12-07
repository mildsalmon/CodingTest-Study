from collections import deque

class Area:
    """
    공간에 대한 클래스
    """
    def __init__(self, n, space):
        self.n = n
        self.space = space
        self.shark_pos = self.get_shark_pos()
        self.ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def get_minimum_distance(self, shark_size):
        """
        상어가 모든 지점으로 가는 최단거리를 구함
        :param shark_size: BabyShark 클래스에 있는 상어 크기
        :return: 최단거리 지도
        """
        x, y = self.shark_pos

        q = deque()
        q.append((x, y))
        distance_map = [[-1] * self.n for _ in range(self.n)]
        distance_map[x][y] = 0

        while q:
            x, y = q.popleft()

            for d in self.ds:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    if distance_map[dx][dy] == -1 and self.space[dx][dy] <= shark_size:
                        distance_map[dx][dy] = distance_map[x][y] + 1
                        q.append((dx, dy))

        return distance_map

    def get_shark_pos(self):
        """
        현재 상어 위치를 요청함.
        :return: 현재 상어 위치
        """
        for i in range(n):
            for j in range(n):
                if self.space[i][j] == 9:
                    self.shark_pos = (i, j)
        return self.shark_pos

    def update_shark_pos(self, x, y, value):
        """
        상어 위치를 업데이트함.
        :param x: 수정할 상어의 x좌표
        :param y: 수정할 상어의 y좌표
        :param value: 수정할 내용 / 0은 상어 지우기, 9는 상어 만들기
        :return:
        """
        self.space[x][y] = value

    def get_space(self):
        """
        현재 남은 물고기 지도를 요청함.
        :return: 물고기 지도
        """
        return self.space


class BabyShark:
    """
    상어에 대한 내용을 담은 클래스
    """
    def __init__(self, eat, size):
        self.eat = eat
        self.size = size

    def find_fish(self, minimum_distance_map, space):
        """
        상어가 먹을 수 있는 크기의 물고기를 찾는다.
        만약, 동일한 크기의 물고기가 존재한다면, 우선순위를 (1. 위, 2. 왼쪽)로 정하고 물고기를 찾는다.
        :param minimum_distance_map: 상어에서 모든 물고기까지 가는 최단거리 지도
        :param space: 물고기 지도
        :return:
        """
        n = len(minimum_distance_map)

        fish = [1e9, 0, 0]

        for i in range(n):
            for j in range(n):
                if minimum_distance_map[i][j] != -1 and 0 < space[i][j] < self.size:
                    if minimum_distance_map[i][j] < fish[0]:
                        fish[0] = minimum_distance_map[i][j]
                        fish[1] = i
                        fish[2] = j

        if fish[0] != 1e9:
            return fish
        else:
            return None

    def eat_shark(self):
        """
        상어가 물고기를 먹는 메소드
        먹은 물고기 수가 상어 크기와 같다면, 상어 크기가 1 커진다.
        :return:
        """
        self.eat += 1

        if self.eat == self.size:
            self.eat = 0
            self.size += 1

    def get_size(self):
        """
        현재 상어의 크기를 요청함.
        :return: 상어의 크기
        """
        return self.size

if __name__ == "__main__":
    n = int(input())
    space = []
    shark_eat = 0
    shark_size = 2

    for i in range(n):
        temp = list(map(int, input().split()))
        space.append(temp)

    time = 0

    area = Area(n, space)
    baby_shark = BabyShark(shark_eat, shark_size)

    while True:
        shark_pos = area.get_shark_pos()
        area.update_shark_pos(shark_pos[0], shark_pos[1], 0)

        minimum_distance_map = area.get_minimum_distance(baby_shark.get_size())
        fish = baby_shark.find_fish(minimum_distance_map, area.get_space())
        # print(fish)
        if fish is not None:
            time += fish[0]
            area.update_shark_pos(fish[1], fish[2], 9)
            baby_shark.eat_shark()
        else:
            break

    print(time)