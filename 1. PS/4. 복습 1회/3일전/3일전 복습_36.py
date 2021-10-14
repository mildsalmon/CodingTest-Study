import bisect

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

a = bisect.bisect_right(array, x)
b = bisect.bisect_left(array, x)

if a - b == 0:
    print(-1)
else:
    print(a - b)