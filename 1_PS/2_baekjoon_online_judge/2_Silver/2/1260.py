from collections import deque

def dfs(graph, v, answer):
    answer.append(v)
    print(v, end=' ')
    for i in graph[v]:
        if i not in set(answer):
            dfs(graph, i, answer)

def bfs(graph, answer):
    q = deque()
    q.append(v)
    answer.append(v)

    while q:
        next_node = q.popleft()
        print(next_node, end=' ')

        for i in graph[next_node]:
            if i not in set(answer):
                answer.append(i)
                q.append(i)

n, m, v = list(map(int, input().split()))

graph = [[] for i in range(n+1)]
# check = [False] * (n+1)
answer_dfs = []
answer_bfs = []


for _ in range(m):
    temp = list(map(int, input().split()))

    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

# 아.. 여기서 정렬을 range(n) 해버려서 틀린걸 다른 곳이 틀린줄알고 30분동안 고생했당...
for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, answer_dfs)
print()
bfs(graph, answer_bfs)

# print(*answer_dfs, sep=' ')
# print(*answer_bfs, sep=' ')

# 144052 KB / 988 ms

'''
'''

# 밑에꺼가 더 빠름
# bool 자료형으로 원소를 지정하여 비교해서 더 빠른건가.

# from collections import deque
#
# def dfs(graph, v, check):
#     # answer.append(v)
#     check[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not check[i]:
#             dfs(graph, i, check)
#
# def bfs(graph, v, check):
#     q = deque()
#     q.append(v)
#     # answer.append(v)
#     check[v] = True
#
#     while q:
#         next_node = q.popleft()
#         print(next_node, end=' ')
#
#         for i in graph[next_node]:
#             if not check[i]:
#                 # answer.append(i)
#                 check[i] = True
#                 q.append(i)
#
# n, m, v = list(map(int, input().split()))
#
# graph = [[] for i in range(n+1)]
# check = [False] * (n+1)
# # answer_dfs = []
# # answer_bfs = []
#
# for _ in range(m):
#     temp = list(map(int, input().split()))
#
#     graph[temp[0]].append(temp[1])
#     graph[temp[1]].append(temp[0])
#
# for i in range(1, n+1):
#     graph[i].sort()
#
# dfs(graph, v, check)
# print()
# check = [False] * (n+1)
# bfs(graph, v, check)
#
# # print(*answer_dfs, sep=' ')
# # print(*answer_bfs, sep=' ')

# 130860 KB / 220 ms