"""
Date    : 2022.04.04
Update  : 2022.04.04
Source  : H-Index.py
Purpose : 정렬, 아이디어
url     : https://programmers.co.kr/learn/courses/30/lessons/42747
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(citations):
    answer = 0
    citations.sort()

    for i, citation in enumerate(citations):
        if citation >= len(citations) - i:
            return len(citations) - i

    return answer

print(solution([3,0,6,1,5]))
print(solution([10,8,5,4,3])) # 4
print(solution([25,8,5,3,3])) # 3
print(solution([ 9, 7, 6, 2,1])) # 3
print(solution([6,6,6,6,6,1])) # 5
