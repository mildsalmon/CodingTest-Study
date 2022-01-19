def bi(start, end):
    if start <= end:
        mid = (end + start) // 2

        if mid == array[mid]:
            answer = mid
        elif mid > array[mid]:
            answer = bi(mid+1, end)
        elif mid < array[mid]:
            answer = bi(start, mid-1)
        return answer
    else:
        return -1

global array

n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array)

array.sort()

answer = bi(start, end)

print(answer)