n = int(input())
array = list(map(int, input().split()))

k = -1

for i in range(n-1):
    if array[i] > array[i+1]:
        k = i

if k == -1:
    print(-1)
else:
    m = 0
    for j in range(k, n):
        if array[k] > array[j]:
            m = j

    array[k], array[m] = array[m], array[k]

    temp = array[k+1:]
    temp.sort(reverse=True)
    array = array[:k+1] + temp

    print(*array, sep=' ')