"""
Date    : 2021.12.03
Update  : 2021.12.04
Source  : 1038.py
Purpose : 숫자를 문자열이라고 생각했을때, 문자열의 문자들은 바로 앞의 숫자보다 작아야한다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def decrease_num(save):
    for i in range(1, 11):
        for j in combinations(range(9, -1, -1), i):
            # combinations에서 1개만 뽑을 때, (1, ) 이렇게 괄호가 쳐지는걸 없애기 위함.
            temp = list(j)
            temp_to_str = ''.join(map(str, temp))

            save.append(int(temp_to_str))

from itertools import combinations

n = int(input())

dp = []

decrease_num(dp)
dp.sort()

# dp의 길이보다 입력된 수가 크다면 -1
if len(dp) <= n:
    print(-1)
else:
    print(dp[n])