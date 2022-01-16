"""
Date    : 2022.01.16
Update  : 2022.01.16
Source  : 14600.py
Purpose : 분할정복 / L-트로미노 / 재귀
url     : https://www.acmicpc.net/problem/14600
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


if __name__ == "__main__":
    k = int(input())
    y, x = list(map(lambda value: int(value)-1, input().split()))

    tile_size = 1 << k
    tile = [[0] * tile_size for _ in range(tile_size)]
    tile[x][y] = -1


    print(*tile[::-1], sep='\n')