"""
Date    : 2022.02.24
Update  : 2022.02.24
Source  : 17214.py
Purpose : 정규식 / 조건많은분기 / 구현 / 문자열 / 파싱
url     : https://www.acmicpc.net/problem/17214
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re

def solution(fx):
    answer = ''

    if fx[0] == 'x':
        fx = '1' + fx

    fx = re.sub(r'(\d+)', r'\1x', fx)
    num = fx.split('x')

    # print(fx)

    if len(num) > 2:
        num[0] = int(num[0]) // 2
    else:
        num[0] = int(num[0])

    if num[0] != 1:
        if num[0] == -1:
            answer += '-'
        else:
            answer += str(num[0])

    if len(num) == 2:
        answer += 'x'
    else:
        answer += 'xx'

    if len(num) == 4:
        num[2] = int(num[2])

        if num[2] != 1:
            if num[2] == -1:
                answer += '-'
            elif num[2] > 0:
                answer += '+' + str(num[2])
            elif num[2] < 0:
                answer += str(num[2])
        else:
            answer += '+'

        answer += 'x'

    # print(answer)
    # print(num)
    print(answer)

if __name__ == "__main__":
    fx = input()
    solution(fx)

if __name__ == "__main__":
    # fx = input()
    # solution(fx)
    solution('2x')
    solution('-12x')
    solution('2x-1')
    solution('10x')
    solution('4x')
    solution('2x+1')
    solution('-2x+1')
    solution('-2x-1')
    solution('-2x-4')
    solution('2')
    solution('-1')
    solution('1')
    solution('-16x+1')
    solution('0')

