"""
Date    : 2022.02.23
Update  : 2022.02.23
Source  : 13022.py
Purpose :
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


from collections import defaultdict

def check_word(s):
    cnt = 0
    str_by_cnt = defaultdict(int)
    flag = False

    for i in range(len(s)):
        if s[i] != 'f' and flag:
            check = sum(str_by_cnt.values())

            if check % 4 != 0:
                return 0
            flag = False

        str_by_cnt[s[i]] += 1

        if s[i] == 'f':
            flag = True

    if flag:
        check = sum(str_by_cnt.values())

        if check % 4 != 0:
            return 0

    return 1


if __name__ == "__main__":
    s = input()
    print(check_word(s))