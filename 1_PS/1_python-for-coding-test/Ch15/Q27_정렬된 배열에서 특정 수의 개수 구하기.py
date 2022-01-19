def bi_sec(start, end, target, array):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        if array[mid] > target:
            end = mid -1
        elif array[mid] < target:
            start = mid + 1
    return 0

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = n-1

pre = bi_sec(start, end, x-1, array)
post = bi_sec(start, end, x+1, array)

answer = (post - 1) - (pre + 1) + 1

if post - pre > 0:
    print(answer)
else:
    print(-1)