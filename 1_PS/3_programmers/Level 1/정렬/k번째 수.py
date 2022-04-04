"""
Date    : 2022.04.04
Update  : 2022.04.04
Source  : k번째 수.py
Purpose : 슬라이싱 / 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/42748
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(array, commands):
    answer = []

    for start, end, point in commands:
        temp = array[start - 1:end]
        temp.sort()
        answer.append(temp[point - 1])

    return answer