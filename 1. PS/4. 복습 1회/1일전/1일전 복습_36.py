from bisect import bisect_left, bisect_right

def bi(array, x):
    left = bisect_left(array, x)
    right = bisect_right(array, x)

    if right - left == 0:
        return -1
    else:
        return right - left

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

print(bi(array, x))