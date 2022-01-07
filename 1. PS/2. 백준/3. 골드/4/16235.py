"""
Date    : 2022.01.06
Update  : 2022.01.07
Source  : 16235.py
Purpose :
url     : https://www.acmicpc.net/problem/16235
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def season(area: list, trees: dict, add_nutrient: list) -> bool:
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
            # 현재 area에 나무들이 있다면,
            if len(trees[i][j]) != 0:
                flag = True
                tree = []
                for key, value in trees[i][j].items():
                    temp = [key] * value
                    tree.extend(temp)
                tree.sort()

                trees[i][j].clear()
                # temp_tree = dict()
                death = 0
                for age in tree:
                    area[i][j] -= age
                    # 양분을 먹지 못하고 죽음
                    if area[i][j] < 0:
                        area[i][j] += age
                        # 여름 대비
                        death += age // 2
                    # 양분을 먹을 수 있음
                    elif area[i][j] >= 0:
                        age += 1
                        if age in trees[i][j]:
                            trees[i][j][age] += 1
                        elif age not in trees[i][j]:
                            trees[i][j][age] = 1

                        if age % 5 == 0:
                            create_trees.append((i, j))
                # 여름
                area[i][j] += death
            # 겨울
            area[i][j] += add_nutrient[i][j]

    # 가을
    """
    시간 초과가 나서 수정해봤는데, 역시나 시간 초과
    생각해보면 이 코드가 밑에 코드보다 더 느릴지도 모르겠다.
    """
    for x, y in create_trees:
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < n and 0 <= dy < n:
                age = 1

                if age in trees[dx][dy]:
                    trees[dx][dy][age] += 1
                elif age not in trees[dx][dy]:
                    trees[dx][dy][age] = 1

    """
    시간 초과
    """
    # for i in range(n):
    #     for j in range(n):
    #         # 아래 if문이 없더라도 trees[i][j]가 없는 경우에는 for문 안으로 들어가지 못한다.
    #         # 다만, 코드의 일관성을 위해 if문을 작성하였다.
    #         if len(trees[i][j]) != 0:
    #             # dict().keys()는 dict()의 원소가 변하면 같이 변하기 때문에 따로 list 객체를 만듬
    #             keys = list(trees[i][j].keys())
    #             # 위 코드(#28)에서 key를 처리하는 방식처럼 처리해도 되지만, 불필요하다 판단되어 key값에 단순 list만 적용함
    #                 # 가을은 새로운 나무의 탄생이다.
    #                 # 새로운 나무는 나이가 무조건 1이다. /
    #                 # 기존 위치의 나무의 나이가 5의 배수인 나무의 갯수만큼 새로운 나무가 태어난다.
    #                 # 따라서 새로운 나무의 나이(age=1)을 key로 5의 배수인 나무의 수를 value로 주면 된다.
    #             for key in keys:
    #                 if key % 5 == 0:
    #                     for d in ds:
    #                         dx = i + d[0]
    #                         dy = j + d[1]
    #
    #                         if 0 <= dx < n and 0 <= dy < n:
    #                             age = 1
    #
    #                             # 봄을 지나고 왔기 때문에 trees에는 age가 1인 나무가 있을 수 없다.
    #                             # 다만, 모든 경우에 오류가 발생하지 않게하기 위해서 아래와 같이 작성하였다.
    #                             if age in trees[dx][dy]:
    #                                 trees[dx][dy][age] += trees[i][j][key]
    #                             elif age not in trees[dx][dy]:
    #                                 trees[dx][dy][age] = trees[i][j][key]

    return flag

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
            count += sum(trees[i][j].values())

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
        # 나무는 어린 나무부터 양분을 먹는다 -> 우선순위 큐로 구현
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