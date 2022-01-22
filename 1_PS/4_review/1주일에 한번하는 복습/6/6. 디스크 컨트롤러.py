"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 6. 디스크 컨트롤러.py
Purpose : heap / sjf
url     : https://programmers.co.kr/learn/courses/30/lessons/42627
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq

def solution(jobs):
    jobs.sort(key=lambda x: [-x[0], -x[1]])

    job_len = len(jobs)
    start, require = jobs.pop()
    acc = start
    total_time = 0

    q = []
    heapq.heappush(q, (require, start))

    while q:
        require, start = heapq.heappop(q)
        acc += require
        total_time += (acc - start)

        while jobs:
            if jobs[-1][0] <= acc:
                heapq.heappush(q, jobs.pop()[::-1])
            else:
                if len(q) == 0:
                    temp = jobs.pop()[::-1]
                    heapq.heappush(q, temp)
                    acc = temp[1]
                break

    return total_time // job_len