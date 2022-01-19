from collections import deque

for tc in range(int(input())):
    n = int(input())
    last_rank = list(map(int, input().split()))

    team = [[] for i in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            team[last_rank[i]].append(last_rank[j])
            indegree[last_rank[j]] += 1

    m = int(input())
    announce_rank = []

    for i in range(m):
        # announce_rank.append(list(map(int, input().split())))
        a, b = list(map(int, input().split()))

        if a in team[b]:
            team[b].remove(a)
            team[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        elif b in team[a]:
            team[a].remove(b)
            team[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True
    now_rank = ''

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        elif len(q) >= 2:
            certain = False
            break

        node = q.popleft()
        now_rank += str(node) + ' '

        for next_node in team[node]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                q.append(next_node)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(now_rank.strip())