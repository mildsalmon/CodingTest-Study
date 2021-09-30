# 볼링공 만들기

from itertools import combinations

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

combination_ball = list(combinations(array, 2))
ball_count = len(combination_ball)

for ball in combination_ball:
    if ball[0] == ball[1]:
        ball_count -= 1

print(ball_count)
