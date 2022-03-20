"""
Date    : 2021.12.14
Update  : 2021.03.21
Source  : 완주하지 못한 선수.py
Purpose : 해시를 사용하여 해결
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(participant, completion):
    hash_sum = 0
    hash_dict = dict()

    for people in participant:
        if people not in hash_dict:
            hash_dict[hash(people)] = people
        hash_sum += hash(people)

    for people in completion:
        hash_sum -= hash(people)

    return hash_dict[hash_sum]
