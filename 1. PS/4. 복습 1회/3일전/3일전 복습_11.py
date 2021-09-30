# Chap 8_DP_1로 만들기

# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 4가지다.
    # X가 5로 나누어 떨어지면, 5로 나눈다
    # X가 3으로 나누어 떨어지면, 3으로 나눈다
    # X가 2로 나누어 떨어지면, 2로 나눈다.
    # X에서 1을 뺀다.

# Input
    # 정수 X가 주어진다.
        # 1 <= X <= 30,000

# Output
    # 연산을 하는 횟수의 최소값을 출력한다.

x = int(input())
array = [0] * (x+1)

array[0] = 0
array[1] = 0

for i in range(2, x+1):
    array[i] = array[i-1]
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2])
    if i % 3 == 0:
        array[i] = min(array[i], array[i//3])
    if i % 5 == 0:
        array[i] = min(array[i], array[i//5])
    array[i] = array[i] + 1

print(array[x])

# 15분 / 성공

# Chap 8_DP_개미 전사

# 개미 전사는 메뚜기 마을의 식량창고를 몰래 공격한다.
# 식량창고는 일직선으로 이어져 있다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며, 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.
# 메뚜기 정찰병은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.

# 들키지 않고 식량창고를 약탈하려면 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

# Input
    # 식량창고의 개수 N
        # 3 <= N <= 100
    # 공백 구분하여 식량창고에 저장된 식량의 개수
        # 0 <= K <= 1000

# Output
    # 개미전사가 얻을 수 있는 식량의 최댓값

n = int(input())
array = list(map(int, input().split()))

for i in range(2, n):
    array[i] = max(array[i] + array[i-2], array[i-1])

print(array[n-1])

# 11분 / 성공
# DP 테이블 안만든게 아쉬움.

