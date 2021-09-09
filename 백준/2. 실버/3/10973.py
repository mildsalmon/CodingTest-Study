n = int(input())
array = list(map(int, input().split()))

for i in range(1, n):
    a = 1e9
    if array[i-1] >= array[i]:
        a = min(a, array[i])