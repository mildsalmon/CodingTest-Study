n = int(input())
array = list(map(int, input().split()))

start = 0
end = n
answer = None

while start <= end:
    mid = (start + end) // 2

    if mid == array[mid]:
        answer = mid
        break

    if mid < array[mid]:
        end = mid - 1
    elif mid > array[mid]:
        start = mid + 1

if answer == None:
    print(-1)
else:
    print(answer)