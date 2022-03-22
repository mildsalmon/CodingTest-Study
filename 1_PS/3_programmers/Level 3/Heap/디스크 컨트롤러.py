"""
Date    : 2022.01.21
Update  : 2022.03.22
Source  : 디스크 컨트롤러.py
Purpose : heap / sjf
url     : https://programmers.co.kr/learn/courses/30/lessons/42627
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq


def solution(jobs):
    print()
    answer = 0
    end = 0
    len_jobs = len(jobs)

    heapq.heapify(jobs)

    while jobs:
        start, elapsed_time = heapq.heappop(jobs)
        end = max(end, start) + elapsed_time
        answer += end - start
        temp = []

        for job in jobs[:]:
            if job[0] <= end:
                heapq.heappush(temp, heapq.heappop(jobs)[::-1])

        if temp:
            elapsed_time, start = heapq.heappop(temp)
            end = max(end, start) + elapsed_time
            answer += end - start

            for job in temp:
                heapq.heappush(jobs, job[::-1])
        print(answer)

    return answer // len_jobs



print(solution([[0, 3], [1, 9], [2, 6]]))               # 9
print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
print(solution([[0, 10]]))                              # 10
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
print(solution([[1, 10], [3, 3], [10, 3]]))             # 9

#### 아래 테케 틀림
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74
###

# 테케 출처
# https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html

# 정확성  테스트
# 테스트 1 〉	실패 (48.01ms, 10.1MB)
# 테스트 2 〉	실패 (32.35ms, 10.1MB)
# 테스트 3 〉	실패 (23.04ms, 10.2MB)
# 테스트 4 〉	실패 (22.86ms, 9.97MB)
# 테스트 5 〉	실패 (36.45ms, 10.1MB)
# 테스트 6 〉	실패 (0.12ms, 10MB)
# 테스트 7 〉	실패 (20.13ms, 10.2MB)
# 테스트 8 〉	실패 (12.35ms, 10.3MB)
# 테스트 9 〉	실패 (3.01ms, 10.2MB)
# 테스트 10 〉	실패 (43.59ms, 10.3MB)
# 테스트 11 〉	실패 (0.02ms, 9.97MB)
# 테스트 12 〉	실패 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	실패 (0.02ms, 10.1MB)
# 테스트 15 〉	실패 (0.01ms, 10.1MB)
# 테스트 16 〉	실패 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	실패 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 9.95MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
#
# 채점 결과
# 정확성: 20.0
# 합계: 20.0 / 100.0