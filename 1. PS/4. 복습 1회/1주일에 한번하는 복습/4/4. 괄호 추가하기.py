"""
Date    : 2022.01.09
Update  : 2022.01.09
Source  : 4. 괄호 추가하기.py
Purpose : 재귀 / 완전 탐색
url     : https://www.acmicpc.net/problem/16637
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def recursive(depth: int, num: list, oper: list, result: int) -> None:
    global answer

    if depth >= len(oper):
        answer = max(answer, result)
        return

    recursive(depth+1, num, oper, oper[depth](result, num[depth+1]))

    if depth+1 < len(oper):
        recursive(depth+2, num, oper, oper[depth](result, oper[depth+1](num[depth+1], num[depth+2])))

def split_oper_num(fx: iter) -> list:
    num = []
    oper = []

    oper_dict = {'+': lambda x, y: x+y,
                 '-': lambda x, y: x-y,
                 '*': lambda x, y: x*y}

    for i in range(len(fx)):
        if i % 2 == 0:
            num.append(int(fx[i]))
        elif i % 2 == 1:
            oper.append(oper_dict[fx[i]])

    return num, oper

if __name__ == "__main__":
    n = int(input())
    fx = input()
    num, oper = split_oper_num(fx)

    answer = -1e9

    recursive(0, num, oper, num[0])

    print(answer)