# ch7_이진 탐색_떡볶이 떡 만들기

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start+end)//2
    total = 0
    for i in range(n):
        if array[i] > mid:
            total += (array[i] - mid)

    if total >= m:
        start = mid + 1
        answer = mid
    elif total < m:
        end = mid - 1

print(answer)