n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)
answer = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for i in range(n):
        if array[i] - mid > 0:
            total += array[i] - mid

    if total < m:
        end = mid - 1
    elif total >= m:
        start = mid + 1
        answer = mid

print(answer)