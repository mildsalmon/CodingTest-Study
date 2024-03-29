"""
Date    : 2022.01.02
Update  : 2022.01.02
Source  : 16637.py
Purpose : 재귀 / 완전탐색 / 브루트포스 / 백트래킹 / DFS
url     : https://www.acmicpc.net/problem/16637
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def recursive(result, i, num, oper) -> None:
    global answer

    if i >= len(oper):
        answer = max(answer, result)
        return

    if i+2 < len(num):
        # B: int = operation(num[i+1], num[i+2], oper[i+1])
        B: int = oper[i+1](num[i+1], num[i+2])

        # recursive(operation(result, B, oper[i]), i+2, num, oper)
        recursive(oper[i](result, B), i+2, num, oper)

    # recursive(operation(result, num[i+1], oper[i]), i+1, num, oper)
    recursive(oper[i](result, num[i+1]), i+1, num, oper)

if __name__ == "__main__":

    n: int = int(input())
    num: list = []
    oper: list = []

    oper_dict = {'+': lambda x, y: x+y,
                 '-': lambda x, y: x-y,
                 '*': lambda x, y: x*y}

    array: list = list(input())

    answer: int = -1e9

    for i, value in enumerate(array):
        if i % 2 == 0:
            num.append(int(value))
        elif i % 2 == 1:
            oper.append(oper_dict[value])

    result: int = num[0]

    recursive(result, 0, num, oper)

    print(answer)