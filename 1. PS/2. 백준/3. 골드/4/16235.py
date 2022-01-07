"""
Date    : 2022.01.06
Update  : 2022.01.07
Source  : 16235.py
Purpose :
url     : https://www.acmicpc.net/problem/16235
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def season(area: list, trees: list, add_nutrient: list) -> bool:
    """
    봄 (필요 매개변수 -> 나무 정보, 땅 정보)
        나무는 자신의 나이만큼 양분을 먹고 나이가 1 증가함.
        하나의 칸에 나무가 여러개면 어린 나무부터 양분먹음
        양분 못먹은 나무는 죽음
    여름 (필요 매개변수 -> 죽은 나무 정보)
        봄에 죽은 나무가 양분으로 변함
    가을 (필요 매개변수 -> 나무 정보)
        나무가 번식함
        번식하는 나무는 나이가 5배수
    겨울 (매년 추가되는 양분 정보)
        땅에 양분 추가

    :param area: 땅 정보
    :param trees: 나무 정보 (2차원 리스트 : 원소는 dict)
    :param add_nutrient: 매년 추가되는 양분 정보
    :return:
    """
    global n

    ds = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    flag = False
    create_trees = []

    # 봄
    for i in range(n):
        for j in range(n):
            trees_items = sorted(list(trees[i][j].items()))
            new_trees = {}
            death = 0

            for index, item in enumerate(trees_items):
                # 현재 area에 나무들이 있다면,
                age, tree_num = item
                flag = True
                """
                아마 시간 초과의 원인이 이 부분이라는 생각이 든다.
                ~~동일한 age가 너무 많이 주어져서 그것을 계산으로 처리하지 않고 하나씩 처리하면 시간초과가 발생하는 것 같다.~~
                아예 나무 여러개를 낱개로 처리하지 말고 개수 카운트를 해서 dict()에 value로 줘야겠다.
                밑에 방식은 나무 낱개 개수만큼 리스트에 넣어줘야하므로 속도저하가 발생하는 것 같다.
                """
                total_age = age * tree_num
                area[i][j] -= total_age

                # 양분을 먹지 못하고 죽음
                if area[i][j] < 0:
                    area[i][j] += total_age
                    survive = area[i][j] // age

                    if survive:
                        area[i][j] -= age * survive
                        death += (age // 2) * (tree_num - survive)
                        age += 1
                        if age in new_trees:
                            new_trees[age] += survive
                        elif age not in new_trees:
                            new_trees[age] = survive
                    else:
                        death += summer(trees_items[index:])
                        break

                # 양분을 먹을 수 있음
                elif area[i][j] >= 0:
                    age += 1

                    if age in new_trees:
                        new_trees[age] += tree_num
                    elif age not in new_trees:
                        new_trees[age] = tree_num

            # 여름
            area[i][j] += death
            trees[i][j] = new_trees
            # 겨울
            area[i][j] += add_nutrient[i][j]

    # 가을
    for i in range(n):
        for j in range(n):
            trees_items = list(trees[i][j].items())
            for key, value in trees_items:
                if key % 5 == 0:
                    for d in ds:
                        dx = i + d[0]
                        dy = j + d[1]
                        age = 1
                        if 0 <= dx < n and 0 <= dy < n:
                            if age in trees[dx][dy]:
                                trees[dx][dy][age] += value
                            elif age not in trees[dx][dy]:
                                trees[dx][dy][age] = value

    return flag


def summer(trees_items):
    answer = 0
    for i in range(len(trees_items)):
        answer += (trees_items[i][0] // 2) * trees_items[i][1]

    return answer

def count_tree(trees: list) -> int:
    """
    현재 나무의 갯수를 세줌.
    :param trees: 나무 정보 (2차원 리스트 : 원소는 deque)
    :return: 나무의 개수
    """
    global n

    count = 0

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for value in trees[i][j].values():
                    count += value

    return count

if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))
    # 초기 모든 칸에는 5만큼의 양분이 있음
    area = [[5]*n for _ in range(n)]
    # 겨울에 추가되는 양분
    add_nutrient = []

    for i in range(n):
        temp = list(map(int, input().split()))
        add_nutrient.append(temp)

    # 각 area별 나무 정보
        # 나무는 어린 나무부터 양분을 먹는다
    # key = age of tree
    # value = tree number
    trees = [[{} for _ in range(n)] for _ in range(n)]

    for i in range(m):
        x, y, age = list(map(int, input().split()))

        if age in trees[x-1][y-1]:
            trees[x-1][y-1][age] += 1
        elif age not in trees[x-1][y-1]:
            trees[x-1][y-1][age] = 1

    # K년동안의 나무 수 변화를 지켜봄
    while k != 0:
        k -= 1

        if not season(area, trees, add_nutrient):
            break

    print(count_tree(trees))