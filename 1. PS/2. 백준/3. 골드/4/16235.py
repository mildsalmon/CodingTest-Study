"""
Date    : 2022.01.06
Update  : 2022.01.06
Source  : 16235.py
Purpose :
url     : https://www.acmicpc.net/problem/16235
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq

def spring(area, q):
    """
    자신의 나이만큼 양분을 먹음 -> 나무()
    :param area:
    :param q:
    :return:
    """
    global n

    for i in range(n):
        for j in range(n):
            temp_q = []
            death_nutrient = 0

            while q[i*n+j]:
                age = heapq.heappop(q[i*n+j])
                # 양분 먹기
                area[i][j] -= age
                if area[i][j] < 0:
                    area[i][j] += age
                    death_nutrient += summer(age)
                else:
                    age += 1
                    temp_q.append(age)

            while temp_q:
                tree = temp_q.pop()
                heapq.heappush(q[i*n+j], tree)

            area[i][j] += death_nutrient

def summer(age):

    return age//2

def fall(q):
    global n

    ds = ((-1, -1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for i in range(n):
        for j in range(n):
            for tree in q[i*n+j]:
                if tree % 5 == 0:
                    for d in ds:
                        dx = i + d[0]
                        dy = j + d[1]
                        if 0 <= dx < n and 0 <= dy < n:
                            new_tree = 1
                            heapq.heappush(q[dx*n+dy], new_tree)

def winter(area, add_nutrient):
    global n

    for i in range(n):
        for j in range(n):
            area[i][j] += add_nutrient[i][j]

def count_tree(q):
    global n

    count = 0

    for i in range(n):
        for j in range(n):
            if len(q[i*n+j]) != 0:
                count += len(q[i*n+j])

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
    q = [[] for _ in range(n*n)]

    for i in range(m):
        x, y, age = list(map(int, input().split()))
        x -= 1
        y -= 1
        heapq.heappush(q[x*n+y], age)

    # K년동안의 나무 수 변화를 지켜봄
    while k != 0:
        k -= 1

        spring(area, q)
        fall(q)
        winter(area, add_nutrient)

    print(count_tree(q))