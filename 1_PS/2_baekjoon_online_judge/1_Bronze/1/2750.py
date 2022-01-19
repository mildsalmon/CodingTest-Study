n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()

print(*array, sep='\n')

# 고인물들은 이렇게 푼다.

print(*sorted(map(int,[*open(0)][1:])))