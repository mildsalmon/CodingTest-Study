"""
Date    : 2022.01.01
Update  : 2022.01.01
Source  : 프린터.py
Purpose : 큐
url     : https://programmers.co.kr/learn/courses/30/lessons/42587
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

def check(priority, qs) -> bool:
    for q in qs:
        if priority < q[1]:
            return False
    return True

def solution(priorities, location) -> int:
    q: deque = deque([(i, p) for i, p in enumerate(priorities)])
    print_num: int = 1

    while q:
        index, priority = q.popleft()

        if check(priority, q):
            if index == location:
                return print_num
            else:
                print_num += 1
        elif not check(priority, q):
            q.append((index, priority))