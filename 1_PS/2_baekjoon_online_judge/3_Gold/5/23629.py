"""
Date    : 2022.02.20
Update  : 2022.02.20
Source  : 23629.py
Purpose :
url     : https://www.acmicpc.net/problem/23629
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re


def change(num):
    result = ''

    for temp in str(num):
        temp = re.sub(r'0', r'ZERO', temp)
        temp = re.sub(r'1', r'ONE', temp)
        temp = re.sub(r'2', r'TWO', temp)
        temp = re.sub(r'3', r'THREE', temp)
        temp = re.sub(r'4', r'FOUR', temp)
        temp = re.sub(r'5', r'FIVE', temp)
        temp = re.sub(r'6', r'SIX', temp)
        temp = re.sub(r'7', r'SEVEN', temp)
        temp = re.sub(r'8', r'EIGHT', temp)
        temp = re.sub(r'9', r'NINE', temp)

        result += temp

    return result


def calculation(re_s, oper):
    expression = f'{re_s[0]}'
    result = re_s[0]

    for i, temp in enumerate(re_s[1:]):
        if len(oper[i]) > 1:
            return 'Madness!'

        if oper[i] == '+':
            result = result + temp
        elif oper[i] == '-':
            result = result - temp
        elif oper[i] == 'x':
            result = result * temp
        elif oper[i] == '/':
            result = int(result / temp)

        expression += f'{oper[i]}{temp}'

    expression += '='
    expression += f'\n{change(result)}'

    return expression


if __name__ == "__main__":
    s = input()

    oper = re.sub(r'[A-Z]', r' ', s).split()
    s = re.sub(r'[+x/=-]', r' ', s)
    re_s = []

    for temp in s.split():
        temp = re.sub(r'ZERO', r'0', temp)
        temp = re.sub(r'ONE', r'1', temp)
        temp = re.sub(r'TWO', r'2', temp)
        temp = re.sub(r'THREE', r'3', temp)
        temp = re.sub(r'FOUR', r'4', temp)
        temp = re.sub(r'FIVE', r'5', temp)
        temp = re.sub(r'SIX', r'6', temp)
        temp = re.sub(r'SEVEN', r'7', temp)
        temp = re.sub(r'EIGHT', r'8', temp)
        temp = re.sub(r'NINE', r'9', temp)

        re_s.append(int(temp))

    result = calculation(re_s, oper)

    if result == 'Madness!':
        print(result)
    else:
        print(result)
