"""
Date    : 2021.12.16
Update  : 2021.12.16
Source  : 6603.py
Purpose : 조합 문제
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def input_check(tc):
    if tc == '0':
        return None
    return tc

from itertools import combinations

if __name__ == "__main__":

    while True:
        temp = input()

        if input_check(temp) is None:
            break
        else:
            k, S = list(temp.split(' ', 1))
            S = list(map(int, S.split(' ')))

            combi = list(combinations(S, 6))

            for c in combi:
                print(*c, sep=' ')
        print()