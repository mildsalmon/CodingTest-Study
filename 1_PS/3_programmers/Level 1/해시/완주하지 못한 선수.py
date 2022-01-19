"""
Date    : 2021.12.14
Update  : 2021.12.14
Source  : 완주하지 못한 선수.py
Purpose : 해시를 사용하여 해결
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(participant, completion):
    """
    여러가지 방법을 생각하다가 시간복잡도 문제때문에 dict()을 사용하여 단순하게 풀었다.
    """
    check = {}
    for part in participant:
        if part in check:
            check[part] += 1
        else:
            check[part] = 1

    for com in completion:
        if com in check:
            check[com] -= 1

    for c in check:
        if check[c] == 1:
            return c



# 다른 사람의 풀이

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer