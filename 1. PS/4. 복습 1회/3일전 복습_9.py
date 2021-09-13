# Ch7_이진 탐색_떡볶이 떡 만들기

# 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 손님은 잘린 부분만 가져간다.

# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값은?

# Input
# 떡의 갯수 N, 떡의 길이 M
    # 1 <= N <= 1,000,000
    # 1 <= M <= 2,000,000,000
# 떡의 개별 높이
    # 떡 높이의 총합은 항상 M 이상
    # 높이는 10억보다 작거나 같다.

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
height = 0

start = 0
end = max(array)

while (start <= end):
    mid = (start + end) // 2 # 절단기의 높이
    result = 0
    for i in range(n):
        if array[i] > mid:
            result = result + array[i] - mid

    if result < m:
        end = mid - 1
    elif result >= m:
        start = mid + 1
        height = mid

print(height)

# 성공 / 16분 44초