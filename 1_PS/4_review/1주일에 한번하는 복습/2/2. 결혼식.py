from collections import deque

if __name__ == "__main__":
    # 동기의 수
    n = int(input())
    # 리스트의 길이
    m = int(input())

    friends = [[] for i in range(n+1)]

    for _ in range(m):
        a, b = list(map(int, input().split()))

        friends[a].append(b)
        friends[b].append(a)

    relation = 0

    q = deque()
    q.append((1, relation))

    visited = [False] * (n+1)
    visited[1] = True

    count = 0

    while q:
        x, relation = q.popleft()

        if relation < 2:
            for friend in friends[x]:
                if not visited[friend]:
                    q.append((friend, relation+1))
                    visited[friend] = True
                    count += 1
        else:
            break

    print(count)