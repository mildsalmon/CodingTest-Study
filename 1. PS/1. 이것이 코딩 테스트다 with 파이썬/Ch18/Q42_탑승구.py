"""
Date    : 2021.11.30
Update  : 2021.11.30
Source  : Q42_탑승구.py
Purpose : 이걸 어떻게 union-find로 풀어야할지 모르겠어서, 구현했다. 딱 테스트케이스만 통과할 수 있는 코드일 것 같기도 하다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

g = int(input())
p = int(input())

boarding_gate = []

for _ in range(p):
    boarding_gate.append(int(input()))

docking = [i for i in range(g+1)]
count = 0

for b_g in boarding_gate:
    while docking[b_g] != b_g:
        b_g -= 1

        if b_g == 0:
            b_g = 1
            break

    if docking[b_g] == b_g:
        docking[b_g] = 0
        count += 1
    elif docking[b_g] == 0:
        break

print(count)