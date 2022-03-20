"""
Date    : 2022.03.16
Update  : 2022.03.20
Source  : 3967.py
Purpose : 백트래킹 / 탐색
url     : https://www.acmicpc.net/problem/3967
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def convert_str_to_num(s):
    return ord(s) - ord('A')


def convert_num_to_str(num):
    return chr(num + ord('A'))


def search_magic_star(search_pos, visited, depth):
    global stars

    if depth == len(search_pos):
        if stars[0][4] + stars[1][3] + stars[2][2] + stars[3][1] + 4 != 26:
            return False
        if stars[0][4] + stars[1][5] + stars[2][6] + stars[3][7] + 4 != 26:
            return False
        if stars[1][1] + stars[1][3] + stars[1][5] + stars[1][7] + 4 != 26:
            return False
        if stars[3][1] + stars[3][3] + stars[3][5] + stars[3][7] + 4 != 26:
            return False
        if stars[1][1] + stars[2][2] + stars[3][3] + stars[4][4] + 4 != 26:
            return False
        if stars[1][7] + stars[2][6] + stars[3][5] + stars[4][4] + 4 != 26:
            return False
        return True

    x, y = search_pos[depth]
    for i in range(12):
        if visited[i]:
            continue
        visited[i] = True
        stars[x][y] = i
        flag = search_magic_star(search_pos, visited, depth+1)
        if flag:
            return True
        stars[x][y] = 'x'
        visited[i] = False


if __name__ == "__main__":
    stars = []
    search_pos = []
    visited = [False for _ in range(12)]

    for i in range(5):
        temp = list(input())
        for j in range(9):
            if temp[j] == '.':
                continue

            if temp[j] == 'x':
                search_pos.append((i, j))
            else:
                index = convert_str_to_num(temp[j])
                visited[index] = True
                temp[j] = index
        stars.append(temp)

    search_magic_star(search_pos, visited, 0)

    for i in range(5):
        for j in range(9):
            if stars[i][j] == '.':
                print('.', end='')
            else:
                print(convert_num_to_str(stars[i][j]), end='')
        print()
    # print(*stars, sep='\n')

