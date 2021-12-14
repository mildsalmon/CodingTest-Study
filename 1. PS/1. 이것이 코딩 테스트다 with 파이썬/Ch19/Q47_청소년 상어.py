"""
Date    : 2021.12.09
Update  : 2021.12.13
Source  : Q46_아기 상어.py
Purpose : dfs로 구현한 것을 클래스로 변경함.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 물고기는 번호와 방향을 갖는다.
    # 방향을 45도 반시계로

# 초기

# 상어는 물고기를 먹고 물고기 방향으로 이동한다.
    # 물고기 먹고 빈칸 만들기

# 물고기도 움직임
    # 이동 x -> 상어가 있거나, 공간 밖
    # 번호가 작은 순서로 이동함.
    # 이동할 수 있을떄까지 45도 회전
    #이동 x면 이동 x
    # 다른 물고기칸으로 이동할떄는 서로 위치를 바꾸는 방식으로

# 물고기 이동 -> 상어 이동

# 상어
    # 방향에 있는 칸을 이동할 수 있고 한 번에 여러 칸을 이동할 수 있음
    # 물고기가 있는칸으로 이동하면, 물고기 먹고 물고기의 방향을 갖는다.
    # 지나가는 칸에 있는 물고기는 먹지 않음
    # 빈 칸으로는 이동하지 못함
        # 이동하던 중 칸이 없으면 집으로 돌아감 ==> 이거를 초기 시작위치인 0,0으로 돌아간다고 이해하고 풀었음

# 상어가 집으로 간 후에는 물고기가 다시 움직임 -> 반복
import copy

class Fish:
    """
    물고기
    """
    def __init__(self, num, direction):
        """
        물고기 번호와 방향을 생성자의 매개변수로 받음
        :param num:
        :param direction:
        """
        self.num = num
        self.direction = direction

    def get_info(self) -> list:
        """
        물고기 전체 정보 반환
        처음에는 get_num, get_direction 메소드를 따로 만들기 번거로워서 만들었는데,
        num 정보만 필요할 경우 이 메소드는 [num, direction]을 반환하므로 더 복잡해져서 잘 안쓰게 되었다.
        :return: [물고기 번호, 물고기 방향]
        """
        return [self.num, self.direction]

    def set_direction(self, new_direction):
        """
        물고기는 현재 방향으로 이동하지 못한다면, 최대 한 바퀴동안 방향을 45도 변경하며 탐색한다.
        이때, 물고기의 방향값이 수정되어야 한다.
        :param new_direction:
        :return:
        """
        self.direction = new_direction

    def get_direction(self) -> int:
        """
        물고기 방향 반환
        :return:
        """
        return self.direction

    def get_num(self) -> int:
        """
        물고기 번호 반환
        :return:
        """
        return self.num

    def set_num(self, num):
        """
        상어가 물고기를 먹었다면, 물고기 번호를 지우거나 (-1), 상어(99)로 바꿔줘야 한다
        :param num:
        :return:
        """
        self.num = num

class Shark:
    """
    상어
    """
    def __init__(self, pos, direction, eat):
        """
        :param pos: 초기 좌표 튜플
        :param direction: 방향
        :param eat: 먹은 물고기 번호 합
        """
        self.pos = pos
        self.direction = direction
        self.eat = eat

    def change_direction(self, new_direction):
        """
        상어 방향을 바꿈
        dfs 매개변수로 상어 방향을 바로 입력해주어서 사용하지는 않음.
        :param new_direction:
        :return:
        """
        self.direction = new_direction

    def get_info(self) -> list:
        """
        상어 정보를 반환
        :return:
        """
        return [self.pos, self.direction, self.eat]

    def change_eat(self, eat):
        """
        상어가 먹은 물고기 수를 갱신
        :param eat:
        :return:
        """
        self.eat = eat

    def get_eat(self) -> int:
        """
        현재까지 먹은 물고기 수를 반환
        :return:
        """
        return self.eat

class Area:
    """
    맵과 관련된 클래스
    맵의 이동, 상어 이동 포함.
    """
    def __init__(self):
        self.ds = ((-1, 0), # 상
              (-1, -1), # 대 (왼상)
              (0, -1), # 왼
              (1, -1), # 대 (왼하)
              (1, 0), # 하
              (1, 1), # 대 (오하)
              (0, 1), # 오
              (-1, 1)) # 대 (오상)
        self.n = 4
        self.game_map = [[None] * self.n for _ in range(self.n)]

    def set_fish(self, x, y, fish):
        """
        맵에 물고기를 저장
        :param x: x좌표
        :param y: y좌표
        :param fish: Fish 객체
        :return:
        """
        self.game_map[x][y] = fish

    def show_map(self):
        """
        간단하게 맵에 위치한 물고기 정보를 확인할 수 있게함.
        :return:
        """
        for i in range(self.n):
            for j in range(self.n):
                print(self.game_map[i][j].get_info(), end=' ')
            print()

    def move(self, game_map):
        """
        상어가 한 번 움직이면, 물고기가 이동해야함.
        dfs를 활용해서, Area 클래스의 인스턴스 객체를 활용하지 않고 매개변수 값을 활용함.
        :param game_map: 이전 물고기들의 움직임이 저장된 지도
        :return:
        """
        fish_moved = [False] * (self.n * self.n + 1)

        for k in range(1, self.n * self.n + 1):
            for i in range(self.n):
                for j in range(self.n):
                    if game_map[i][j].get_num() == k and not fish_moved[k]:
                        for dk in range(len(self.ds)):
                            next_pos = (game_map[i][j].get_direction() + dk) % len(self.ds)
                            d = self.ds[next_pos]
                            dx = i + d[0]
                            dy = j + d[1]

                            if 0 <= dx < self.n and 0 <= dy < self.n:
                                if game_map[dx][dy].get_num() != 99:
                                    game_map[i][j].set_direction(next_pos)
                                    game_map[i][j], game_map[dx][dy] = game_map[dx][dy], game_map[i][j]
                                    fish_moved[k] = True
                                    # print(*fishs, sep='\n')
                                    # print()
                                    break

    def get_map(self) -> list:
        """
        현재 지도에 저장된 물고기 정보를 반환
        처음 1회만 사용됨.
        :return:
        """
        return self.game_map

    def dfs(self, x, y, shark_eat, shark_direction, copy_map):
        """
        상어 이동 코드
        어느 클래스에 포함시켜야할지 고민이었다. 차라리 클래스 밖에 함수로 존재시키는 것이 더 좋았을지도 모르겠다.
        이 함수에서는 인자로 전달해준 값을 갱신하여 비교를 진행하므로 인스턴스 변수의 사용이 불필요하다.
        :param x:
        :param y:
        :param shark_eat:
        :param shark_direction:
        :param copy_map:
        :return:
        """
        new_copy_map = copy.deepcopy(copy_map)
        shark_eat += new_copy_map[x][y].get_num()
        new_copy_map[x][y].set_num(99)
        self.move(new_copy_map)
        eat_list = []
        shark_eat_list = []

        for i in range(1, self.n):
            next_pos = shark_direction
            d = self.ds[next_pos]
            dx = x + d[0] * i
            dy = y + d[1] * i

            if 0 <= dx < self.n and 0 <= dy < self.n:
                if new_copy_map[dx][dy].get_num() != -1:
                    eat_list.append((dx, dy))

        new_copy_map[x][y].set_num(-1)

        if len(eat_list) == 0:
            return shark_eat

        for eat in eat_list:
            shark_direction = new_copy_map[eat[0]][eat[1]].get_direction()
            shark_eat_list.append(self.dfs(eat[0], eat[1], shark_eat, shark_direction, new_copy_map))

        return max(shark_eat_list)


if __name__ == "__main__":
    area = Area()

    for i in range(area.n):
        temp = list(map(int, input().split()))

        for j in range(area.n):
            fish = Fish(temp[j*2], temp[j*2+1]-1)
            area.set_fish(i, j, fish)

    # area.show_map()

    shark = Shark((0,0), area.game_map[0][0].get_direction(), 0)

    # print(shark.get_info())
    shark_info = shark.get_info()

    shark.change_eat(area.dfs(shark_info[0][0], shark_info[0][1], shark_info[2], shark_info[1], area.get_map()))

    print(shark.get_eat())
