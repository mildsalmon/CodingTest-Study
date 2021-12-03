"""
Date    : 2021.12.03
Update  : 2021.12.03
Source  : Q45_최종 순위.py
Purpose : 위상 정렬을 이용하여 해결. (위상정렬의 cycle과 결과값이 여러개일 경우를 고려해야함)
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

for test_case in range(int(input())):
    n = int(input())
    # 방향 그래프를 표현하기 위해 인접 행렬을 생성함.
    graph = [[False]*(n+1) for i in range(n+1)]
    # 진입차수
    indegree = [0] * (n+1)

    last_rank = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            # 앞 등수는 뒷 등수를 가리킴
            # 1등 -> 2등,3등,4등,5등
                # 2,3,4,5등의 진입차수를 증가시킴
            # 앞 등수가 뒷 등수를 가리키는 것을 true처리함.
                # 1등 -> 2등 (ok), 2등 -> 1등 (x)
            graph[last_rank[i]][last_rank[j]] = True
            indegree[last_rank[j]] += 1

    m = int(input())

    for i in range(m):
        a, b = list(map(int, input().split()))
        # 순위가 변경되면, 방향 그래프의 방향을 바꿈
        if graph[b][a]:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1

    q = deque()

    # 진입차수가 0인 것만 q에 집어넣음
    # 이 문제는 순위라서 진입차수가 0인 것이 한개여야함.
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    # 데이터의 일관성이 없는 경우
    cycle = False
    # 확실한 순위를 찾을 수 없는 경우
    consistency = True
    new_rank = []

    for i in range(n):
        # q에 아무것도 없다면, cycle인 것
        if len(q) == 0:
            cycle = True
            break
        # q가 2개 이상이면, 순위표가 여러개 나올 수 있는 것
        elif len(q) >= 2:
            consistency = False
            break

        team = q.popleft()
        new_rank.append(team)

        for j, next_team in enumerate(graph[team]):
            if next_team:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not consistency:
        print("?")
    else:
        print(*new_rank, sep=' ')