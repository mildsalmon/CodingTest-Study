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

    for i in range(max(citations)):
        quotation = [0, 0]
        for j, citation in enumerate(citations):
            if citation >= i:
                quotation[0] = len(citations[j:])
                quotation[1] = len(citations[:j])
                break
        if quotation[0] >= i and quotation[1] <= i:
            answer = i

    return answer

solution([3,0,6,1,5])
solution([10,8,5,4,3]) # 4
solution([25,8,5,3,3]) # 3
solution([ 9, 7, 6, 2,1]) # 3
