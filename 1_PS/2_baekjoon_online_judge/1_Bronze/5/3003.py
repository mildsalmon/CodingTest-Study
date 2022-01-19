array = list(map(int, input().split()))
peaces = [1, 1, 2, 2, 2, 8]
result = [0] * 6

for i in range(len(peaces)):
    result[i] = peaces[i] - array[i]

print(*result, sep=' ')