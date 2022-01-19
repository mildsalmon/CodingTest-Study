n, c = list(map(int, input().split()))
array = []

for i in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]

answer = 0

while start <= end:
    mid = (start + end) // 2
    house = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= house + mid:
            count += 1
            house = array[i]

    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
