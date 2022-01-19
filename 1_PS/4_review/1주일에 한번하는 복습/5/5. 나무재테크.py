"""
Date    : 2022.01.15
Update  : 2022.01.15
Source  : 1520.py
Purpose :
url     : https://www.acmicpc.net/problem/1520
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def season(area, trees):
    global n, add_nutrient

    ds = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    create_trees = {}

    # 봄
    for i in range(n):
        for j in range(n):
            death = 0
            if len(trees[i][j]):
                tree_items = sorted(trees[i][j].items())
                new_tree = {}

                for index, item in enumerate(tree_items):
                    age, tree_num = item
                    total_tree = age * tree_num
                    area[i][j] -= total_tree

                    if area[i][j] < 0:
                        area[i][j] += total_tree
                        possible_tree_num = area[i][j] // age

                        if possible_tree_num:
                            area[i][j] -= (age * possible_tree_num)
                            death += (age//2) * (tree_num - possible_tree_num)
                            age += 1
                            add_dict(age, possible_tree_num, new_tree)

                            fall(age, (i, j), possible_tree_num, create_trees)

                        else:
                            death += sum(list(map(lambda x: (x[0]//2) * x[1], tree_items[index:])))
                            break

                    elif area[i][j] >= 0:
                        age += 1
                        add_dict(age, tree_num, new_tree)

                        fall(age, (i, j), tree_num, create_trees)

                trees[i][j] = new_tree
            area[i][j] += death
            area[i][j] += add_nutrient[i][j]

    # 가을
    for key, value in create_trees.items():
        x, y = key
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < n and 0 <= dy < n:
                add_dict(1, value, trees[dx][dy])


def fall(key, xy, value, iterable):
    if key % 5 == 0:
        add_dict(xy, value, iterable)

def add_dict(key: int, value: int, iterator: dict) -> None:
    if key in iterator:
        iterator[key] += value
    elif key not in iterator:
        iterator[key] = value

def count_tree(trees):
    global n

    result = 0

    for i in range(n):
        for j in range(n):
            result += sum(trees[i][j].values())

    return result

if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))

    area = [[5] * n for _ in range(n)]
    add_nutrient = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        add_nutrient.append(temp)

    trees = [[{} for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        i, j, age = list(map(int, input().split()))

        add_dict(age, 1, trees[i-1][j-1])

    for year in range(k):
        season(area, trees)

    print(count_tree(trees))