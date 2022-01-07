"""
Date    : 2022.01.06
Update  : 2022.01.07
Source  : 16235.py
Purpose : 구현 / 시간복잡도 / dict / count
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
    # 만약 좌표평면에 나무가 하나도 없다면 나무는 번식도 성장도 못함.
    # 따라서 종료시켜야함.
    flag = False
    create_trees = {}

    # 봄
    for i in range(n):
        for j in range(n):
            """
            좌표별로 저장된 나무 dict를 분석한다.
            dict에 저장된 값은 정렬을 통해 어린 나무부터 처리되도록 한다.
            아래의 trees_items, new_trees, death는 좌표별로 새로운 값으로 갱신해야한다.
            """
            trees_items = sorted(list(trees[i][j].items()))
            new_trees = {}
            death = 0

            for index, item in enumerate(trees_items):
                age, tree_num = item
                flag = True
                """
                ## 시간초과의 원인 !
                좌표별로 나무를 관리하는 방법을 생각할 수 있다.
                이때, 단순히 deque로 나무들을 모두 넣어주면 가을에 증폭되는 1번 나무들을 제어할 수 없어서 시간초과가 발생한다.
                따라서, dict의 key:value를 (나무의 나이:나무의 개수)로 관리하면 봄에 나무의 개수만큼 반복이 도는게 아니라 나무의 나이만큼만 반복이 돌게된다.
                """
                # 현재 나이를 가지는 모든 나무를 곱함.
                total_age = age * tree_num
                area[i][j] -= total_age

                if area[i][j] < 0:
                    """
                    # 현재 나이를 가지는 모든 나무에 영양분을 못줌
                        1. 이전에 제거한 영양분을 복구한다.
                        2. 현재 나이의 나무는 최대 몇개 심을 수 있는지 구함.
                            1. 심을 수 있는 나무가 1개 이상인 경우
                                1. 땅에 (심을 수 있는 나무 * 현재 나무의 나이)를 뺀다.
                                2. 여름을 대비하기 위해 죽은 나무를 분해한다.
                                3. 나무의 나이를 증가시키고 심을 수 있는 나무의 개수로 업데이트한다.
                            2. 심을 수 있는 나무가 0개인 경우
                                1. 현재 나무부터 뒤에 있는 모든 나무를 분해한다.
                                2. break로 현재 좌표를 탈출한다.
                    """
                    area[i][j] += total_age
                    survive = area[i][j] // age
                    if survive:
                        area[i][j] -= age * survive
                        # 여름 대비
                        death += (age // 2) * (tree_num - survive)
                        age += 1
                        if age in new_trees:
                            new_trees[age] += survive
                        elif age not in new_trees:
                            new_trees[age] = survive

                        # 가을 대비
                        if age % 5 == 0:
                            if (i, j) in create_trees:
                                create_trees[(i, j)] += survive
                            elif (i, j) not in create_trees:
                                create_trees[(i, j)] = survive
                    else:
                        # 여름 대비
                        death += summer(trees_items[index:])
                        break

                elif area[i][j] >= 0:
                    """
                    # 현재 나이를 가지는 모든 나무에 영양분을 줄 수 있음
                        1. 나무의 나이를 증가하고 나무의 개수를 업데이트한다.
                    """
                    age += 1

                    if age in new_trees:
                        new_trees[age] += tree_num
                    elif age not in new_trees:
                        new_trees[age] = tree_num

                    # 가을 대비
                    """
                    가을을 따로 2중 for문을 다시 써서 처리하는건 비효율적으로 보인다.
                    따라서 시간 절약을 위해 여기서 가을 대비를 하자.
                    """
                    if age % 5 == 0:
                        if (i, j) in create_trees:
                            create_trees[(i, j)] += tree_num
                        elif (i, j) not in create_trees:
                            create_trees[(i, j)] = tree_num
            """
            마지막으로 새로 갱신한 나무 dict로 현재 좌표를 업데이트하면 된다.
            """
            trees[i][j] = new_trees
            # 여름
            """
            여름에는 분해된 나무들을 더하기만 하면 된다.
            """
            area[i][j] += death

            # 겨울
            area[i][j] += add_nutrient[i][j]

    # 가을
    for key, value in create_trees.items():
        x, y = key

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]
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