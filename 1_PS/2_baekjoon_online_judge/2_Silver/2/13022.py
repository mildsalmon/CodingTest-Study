"""
Date    : 2022.02.23
Update  : 2022.02.23
Source  : 13022.py
Purpose :
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re

def solution(text):

    pattern = "(wolf"
    for i in range(2, 13):
        pattern += "|w{}{}{}o{}{}{}l{}{}{}f{}{}{}"\
                .format('{', i, '}','{', i, '}','{', i, '}','{', i, '}',)
    pattern += ")"

    extra = re.sub(pattern, "", text)
    if len(extra) > 0:
        print(0)
    else:
        print(1)

solution('wolwolff')
solution('wolf')
solution('wwolfolf')
solution('wwwoolllfff')
solution('wwolfolf')
solution('wfol')
solution('wolfwwoollffwolf')
solution('wolf')
solution('wwoollff')
solution('wwwooolllfff')
    # '''
    # 0
    # 1
    # 0
    # 0
    # 0
    # 0
    # 0
    # 1
    # 1
    # 1
    # 1
    # '''