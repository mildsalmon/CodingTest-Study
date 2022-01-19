n, c = list(map(int, input().split()))

array = []

for i in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]

while start <= end:
    mid = (start + end) // 2

    pos = array[0]
    count = 0

    for a in array:
        if pos <= a:
            pos = a + mid
            count += 1

    if count >= c:
        start = mid + 1
        answer = mid
    elif count < c:
        end = mid - 1

print(answer)