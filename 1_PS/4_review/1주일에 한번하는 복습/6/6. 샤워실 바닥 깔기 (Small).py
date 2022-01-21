"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 14600.py
Purpose : 트리 / 분할 정복
url     : https://www.acmicpc.net/problem/14600
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def check_divide_tile(tile_size: int, x: int, y: int) -> bool:
    global room

    for i in range(x, x+tile_size):
        for j in range(y, y+tile_size):
            if room[i][j] != 0:
                return False
    return True


def recursive(tile_size: int, room: list, x: int, y: int) -> None:
    global tile_num

    check_tile_size = tile_size >> 1
    tile_num += 1

    if check_divide_tile(check_tile_size, x, y):
        room[x + check_tile_size - 1][y + check_tile_size - 1] = tile_num
    if check_divide_tile(check_tile_size, x, y + check_tile_size):
        room[x + check_tile_size - 1][y + check_tile_size] = tile_num
    if check_divide_tile(check_tile_size, x + check_tile_size, y):
        room[x + check_tile_size][y + check_tile_size - 1] = tile_num
    if check_divide_tile(check_tile_size, x + check_tile_size, y + check_tile_size):
        room[x + check_tile_size][y + check_tile_size] = tile_num

    if tile_size == 2:
        return

    recursive(check_tile_size, room, x, y)
    recursive(check_tile_size, room, x, y + check_tile_size)
    recursive(check_tile_size, room, x + check_tile_size, y)
    recursive(check_tile_size, room, x + check_tile_size, y + check_tile_size)


if __name__ == "__main__":
    k = int(input())
    x, y = list(map(lambda x: int(x)-1, input().split()))
    tile_size = k << 1

    room = [[0] * tile_size for _ in range(tile_size)]
    room[y][x] = -1

    tile_num = 0

    recursive(tile_size, room, 0, 0)

    for i in range(tile_size-1, -1, -1):
        for j in range(tile_size):
            print(room[i][j], end=' ')
        print()