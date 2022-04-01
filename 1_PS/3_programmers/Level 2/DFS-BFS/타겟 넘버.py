"""
Date    : 2021.04.01
Update  : 2021.04.01
Source  : 타겟 넘버.py
Purpose : DFS
url     : https://programmers.co.kr/learn/courses/30/lessons/43165
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(depth, numbers, target):
    global answer

    if depth == len(numbers):
        if target == sum(numbers):
            answer += 1
        return

    temp = numbers[:]
    temp[depth] = -temp[depth]
    dfs(depth + 1, temp, target)
    temp[depth] = -temp[depth]
    dfs(depth + 1, temp, target)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(0, numbers, target)

    return answer