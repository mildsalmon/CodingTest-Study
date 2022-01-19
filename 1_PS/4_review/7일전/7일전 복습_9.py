# Ch7_이진탐색_떡볶이 떡 만들기

# 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이(H)를 지정하면 떡을 한번에 절단한다. 높이가 H보다 긴 떡은 잘리고 낮으면 잘리지 않는다.
# 손님은 잘린 떡의 길이만큼 가져간다.
# 손님이 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위한 절단기 높이의 최대값을 구하라

# Input
    # 떡의 개수 N, 떡의 길이 M
        # 1 <= N <= 1,000,000
        # 1 <= M <= 2,000,000,000
    # 떡의 개별 높이 / 떡의 총합은 항상 M 이상
        # 높이는 10억보다 작거나 같은 양의 정수

# Output
    # M만큼의 떡을 가져가기 위해 설정할 수 있는 높이의 최댓값

n, m = list(map(int, input().split()))
arrays = list(map(int, input().split()))

start = 0
end = max(arrays)

answer = 0

while (start <= end):
    mid = (start + end)//2
    result = 0

    for array in arrays:
        if array > mid:
            result += (array-mid)

    if result < m:
        end = mid - 1
    elif result >= m:
        start = mid + 1
        answer = mid

print(answer)

# 14분 / pass