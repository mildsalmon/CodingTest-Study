"""
Date    : 2022.03.04
Update  : 2022.03.04
Source  : 14499.py
Purpose : 객체지향 프로그래밍 (캡슐화, 추상화 애매함, 상속x, 다형성x)
url     : https://www.acmicpc.net/problem/14499
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline


class Dice:
    def __init__(self):
        """
        :param nums: 주사위에 적힌 번호
        :param top, bottom, front, back, right, left: 현재 각 pos의 인덱스
        """
        self.nums = [0 for _ in range(6)]
        self.top_index = 0
        self.bottom_index = 5
        self.front_index = 4
        self.back_index = 1
        self.right_index = 2
        self.left_index = 3

    def get_top(self) -> int:
        """
        현재 주사위의 top 위치에 적힌 번호를 반환
        """
        return self.nums[self.top_index]

    def put_bottom(self, array: list, x: int, y: int):
        """
        현재 array의 값에 따라 다르게 array의 값을 변경해줘야함.
         따라서, array를 iterable객체로 parameter를 받음

        :param array: 지도 정보
        :param x: 현재 x축
        :param y: 현재 y축
        """
        if array[x][y] == 0:
            # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0인 경우
            array[x][y] = self.nums[self.bottom_index]
        else:
            # 0이 아닌 경우
            self.nums[self.bottom_index] = array[x][y]
            array[x][y] = 0

    def roll(self, d: int):
        """
        주사위 굴리기
         미리 주사위의 인덱스를 지역변수로 저장하고 self변수를 변경해줌

        :param d: 주사위가 굴러갈 방향
        """
        # 0 동 1 서 2 북 3 남
        top = self.top_index
        bottom = self.bottom_index
        right = self.right_index
        left = self.left_index
        front = self.front_index
        back = self.back_index

        if d == 0:
            self.top_index = left
            self.bottom_index = right
            self.right_index = top
            self.left_index = bottom
        if d == 1:
            self.top_index = right
            self.bottom_index = left
            self.right_index = bottom
            self.left_index = top
        if d == 2:
            self.top_index = front
            self.bottom_index = back
            self.front_index = bottom
            self.back_index = top
        if d == 3:
            self.top_index = back
            self.bottom_index = front
            self.front_index = top
            self.back_index = bottom

    def __str__(self):
        return f"top = {self.top_index}번, {self.nums[self.top_index]}, " \
               f"bottom = {self.bottom_index}번, {self.nums[self.bottom_index]}, " \
               f"right = {self.right_index}번, {self.nums[self.right_index]}, " \
               f"left = {self.left_index}번, {self.nums[self.left_index]}, " \
               f"front = {self.front_index}번, {self.nums[self.front_index]}, " \
               f"back = {self.back_index}번, {self.nums[self.back_index]}"


if __name__ == "__main__":
    n, m, x, y, k = list(map(int, input().split()))
    array = [list(map(int, input().split())) for _ in range(n)]
    commands = list(map(lambda x: int(x)-1, input().split()))
    dice = Dice()

    ds = ((0, 1), (0, -1), (-1, 0), (1, 0))

    for command in commands:
        dx = x + ds[command][0]
        dy = y + ds[command][1]

        if 0 <= dx < n and 0 <= dy < m:
            x, y = dx, dy

            dice.roll(command)
            dice.put_bottom(array, x, y)
            print(dice.get_top())

            # print(dice)
            # print(array)
