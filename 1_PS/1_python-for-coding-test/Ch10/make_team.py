def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]


def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)

    if a < b:
        team[b] = a
    else:
        team[a] = b


n, m = map(int, input().split())

array = []
team = [0] * (n + 1)

for i in range(1, n + 1):
    team[i] = i

for i in range(m):
    c, a, b = list(map(int, input().split()))
    array.append([c, a, b])

for i in range(m):
    c, a, b = array[i]

    if c == 0:
        union_team(team, a, b)
    elif c == 1:
        if find_team(team, a) == find_team(team, b):
            print("YES")
        else:
            print("NO")

# 20분 4초 / Pass / Time out