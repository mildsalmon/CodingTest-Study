"""
Date    : 2022.01.06
Update  : 2022.01.06
Source  : 16235.py
Purpose :
url     : https://www.acmicpc.net/problem/16235
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque
import sys

input = sys.stdin.readline

def season(area: list, q: list, add_nutrient: list) -> bool:
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
    :param q: 나무 정보 (2차원 리스트 : 원소는 deque)
    :param add_nutrient: 매년 추가되는 양분 정보
    :return:
    """
    global n

    ds = ((-1, -1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    create_tree = []
    flag = False

    for i in range(n):
        for j in range(n):
            # 봄
            if len(q[i*n+j]) != 0:
                flag = True
                save_end_point = len(q[i*n+j])
                end_point = 0
                death_nutrient = 0

                while save_end_point > end_point:
                    end_point += 1
                    age = q[i*n+j].popleft()
                    # 양분 먹기
                    area[i][j] -= age
                    if area[i][j] < 0:
                        area[i][j] += age
                        death_nutrient += age // 2
                    else:
                        age += 1
                        q[i*n+j].append(age)

                        # 시간 단축을 위해 가을에 번식할 나무를 미리 선정함
                            # 이렇게 해도 python에서는 시간초과...
                        if age % 5 == 0:
                            create_tree.append((i, j))
                # 여름
                area[i][j] += death_nutrient
            # 겨울
                # 시간 단축을 위해 한꺼번에 처리함. (그런데, 이렇게 해도 python에서는 시간초과가 뜬다)
                # 이미 지나간 i, j 좌표의 땅의 양분은 이후 봄, 여름, 가을에 영향을 주지 않기 때문에 봄, 여름과 같이 처리함.
            area[i][j] += add_nutrient[i][j]

    # 만약 area에 나무가 하나도 없다면 나무는 더 생기지 않으므로 아예 종료하는게 맞음.
    if not flag:
        return False

    # 가을
    for i, j in create_tree:
        for d in ds:
            dx = i + d[0]
            dy = j + d[1]
            if 0 <= dx < n and 0 <= dy < n:
                new_tree = 1
                # 새로운 나무는 맨 앞에 추가.
                q[dx*n+dy].appendleft(new_tree)

    return True

def count_tree(q: list) -> int:
    """
    현재 나무의 갯수를 세줌.
    :param q: 나무 정보 (2차원 리스트 : 원소는 deque)
    :return: 나무의 개수
    """
    global n

    count = 0

    for i in range(n*n):
        if len(q[i]) != 0:
            count += len(q[i])

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
    # 나무 정보를 2차원 배열로 받기에는 조금 복잡해져서 1차원 배열로 받음
        # 나무는 어린 나무부터 양분을 먹는다 -> 우선순위 큐로 구현
    q = [deque() for _ in range(n*n)]
    temp_trees = [[] for _ in range(n*n)]

    for i in range(m):
        x, y, age = list(map(int, input().split()))
        x -= 1
        y -= 1
        temp_trees[x*n+y].append(age)

    for i in range(n):
        for j in range(n):
            if len(temp_trees[i*n+j]) != 0:
                # 우선순위 큐를 사용하지 못하므로 deque에 나무를 집어넣을때 나이순으로 정렬을 시도해야함.
                age = sorted(temp_trees[i*n+j])
                q[i*n+j].extend(age)

    # K년동안의 나무 수 변화를 지켜봄
    while k != 0:
        k -= 1

        if not season(area, q, add_nutrient):
            break

    print(count_tree(q))