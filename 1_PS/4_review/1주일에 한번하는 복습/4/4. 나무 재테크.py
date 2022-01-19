"""
Date    : 2022.01.10
Update  : 2022.01.10
Source  : 4. 나무 재테크.py
Purpose :
url     : https://www.acmicpc.net/problem/16235
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def season(trees):
    global n, add_nutrient

    ds = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    create_trees = dict()

    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                trees_info = list(trees[i][j].items())
                trees_info.sort()
                temp_trees = {}
                death = 0

                for index, info in enumerate(trees_info):
                    age, tree_count = info
                    total_age = age * tree_count
                    area[i][j] -= total_age
                    flag = True

                    if area[i][j] < 0:
                        # 죽음
                        area[i][j] += total_age
                        possible_count = area[i][j] // age

                        if possible_count == 0:
                            # 뒤에것도 불가능
                            death_count = tree_count
                            death += (age // 2) * death_count
                            continue
                        else:
                            total_possible_age = age * possible_count
                            area[i][j] -= total_possible_age
                            death_count = tree_count - possible_count
                            death += (age // 2) * death_count
                            age += 1

                            if age in temp_trees:
                                temp_trees[age] += possible_count
                            elif age not in temp_trees:
                                temp_trees[age] = possible_count
                            flag = False
                    else:
                        age += 1

                        if age in temp_trees:
                            temp_trees[age] += tree_count
                        elif age not in temp_trees:
                            temp_trees[age] = tree_count

                    if age % 5 == 0:
                        if (i, j) in create_trees:
                            if flag:
                                create_trees[(i, j)] += tree_count
                            else:
                                create_trees[(i, j)] += possible_count
                        elif (i, j) not in create_trees:
                            if flag:
                                create_trees[(i, j)] = tree_count
                            else:
                                create_trees[(i, j)] = possible_count

                trees[i][j] = temp_trees
                area[i][j] += death
            area[i][j] += add_nutrient[i][j]

    for xy, count in create_trees.items():
        x, y = xy
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]
            if 0 <= dx < n and 0 <= dy < n:
                if 1 in trees[dx][dy]:
                    trees[dx][dy][1] += count
                elif 1 not in trees[dx][dy]:
                    trees[dx][dy][1] = count

def check_trees(trees):
    global n

    count = 0

    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                count += sum(trees[i][j].values())

    return count

if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))

    area = [[5] * n for _ in range(n)]

    add_nutrient = []

    for i in range(n):
        temp = list(map(int, input().split()))
        add_nutrient.append(temp)

    trees = [[dict() for _ in range(n)] for _ in range(n)]

    for i in range(m):
        x, y, age = list(map(int, input().split()))
        x -= 1
        y -= 1
        if age in trees[x][y]:
            trees[x][y][age] += 1
        elif age not in trees[x][y]:
            trees[x][y][age] = 1

    for _ in range(k):
        season(trees)

    print(check_trees(trees))