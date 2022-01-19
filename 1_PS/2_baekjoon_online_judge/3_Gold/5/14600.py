"""
Date    : 2022.01.16
Update  : 2022.01.16
Source  : 14600.py
Purpose : 분할정복 / L-트로미노 / 재귀
url     : https://www.acmicpc.net/problem/14600
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def check_tile(size: int, x: int, y: int) -> bool:
    global tile

    for i in range(x, x+size):
        for j in range(y, y+size):
            if tile[i][j] != 0:
                return False
    return True

def fill_tile(tile_num: int, tile: list, size: int, x: int, y: int) -> int:
    tile_num += 1
    temp_size = size >> 1
    if check_tile(temp_size, x, y):
        tile[temp_size + x - 1][temp_size + y - 1] = tile_num
    if check_tile(temp_size, x, y+temp_size):
        tile[temp_size + x - 1][temp_size + y] = tile_num
    if check_tile(temp_size, x+temp_size, y):
        tile[temp_size + x][temp_size + y - 1] = tile_num
    if check_tile(temp_size, x+temp_size, y+temp_size):
        tile[temp_size + x][temp_size + y] = tile_num

    if size == 2:
        return tile_num

    tile_num = fill_tile(tile_num, tile, temp_size, x, y)
    tile_num = fill_tile(tile_num, tile, temp_size, x, y+temp_size)
    tile_num = fill_tile(tile_num, tile, temp_size, x+temp_size, y)
    tile_num = fill_tile(tile_num, tile, temp_size, x+temp_size, y+temp_size)

    return tile_num

if __name__ == "__main__":
    k = int(input())
    y, x = list(map(lambda value: int(value)-1, input().split()))

    tile_size = 1 << k
    tile = [[0] * tile_size for _ in range(tile_size)]
    tile[x][y] = -1

    fill_tile(0, tile, tile_size, 0, 0)

    # print(*tile[::-1], sep='\n')
    # ' '.join()의 인자값은 iterable 객체이다. 다만, iterable 객체 안의 값들은 문자열들이여야 한다.
    print(*map(lambda x: ' '.join(map(str, x)), tile[::-1]), sep='\n')