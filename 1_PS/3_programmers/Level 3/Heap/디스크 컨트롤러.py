"""
Date    : 2022.01.21
Update  : 2022.03.27
Source  : 디스크 컨트롤러.py
Purpose : heap / sjf
url     : https://programmers.co.kr/learn/courses/30/lessons/42627
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq


def solution(jobs):
    total_time = 0
    answer = 0
    wait_q = []
    jobs.sort()
    wait_q.append(jobs[0])
    visited = [False for _ in range(len(jobs))]
    visited[0] = True

    while wait_q:
        start_time, time = heapq.heappop(wait_q)
        total_time = max(total_time, start_time) + time
        answer += total_time - start_time

        if visited.count(True) == len(visited):
            break

        temp = []
        temp_i = 1e9

        for i, job in enumerate(jobs[:]):
            if not visited[i] and job[0] <= total_time:
                temp.append(job + [i])
            elif not visited[i]:
                temp_i = min(i, temp_i)

        if len(temp) == 0:
            temp.append(jobs[temp_i] + [temp_i])

        temp.sort(key=lambda x: (x[1], x[0]))
        heapq.heappush(wait_q, temp[0][:2])
        visited[temp[0][2]] = True

    return answer // len(jobs)


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
# 테스트 1 〉	통과 (0.69ms, 10.1MB)
# 테스트 2 〉	통과 (0.67ms, 10.2MB)
# 테스트 3 〉	통과 (0.71ms, 9.95MB)
# 테스트 4 〉	통과 (0.72ms, 10MB)
# 테스트 5 〉	통과 (0.70ms, 10.1MB)
# 테스트 6 〉	통과 (0.03ms, 9.95MB)
# 테스트 7 〉	통과 (0.50ms, 10.3MB)
# 테스트 8 〉	통과 (0.41ms, 10.1MB)
# 테스트 9 〉	통과 (0.18ms, 9.97MB)
# 테스트 10 〉	통과 (0.86ms, 10MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.02ms, 9.96MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.02ms, 10MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.02ms, 10MB)
# 테스트 20 〉	통과 (0.02ms, 10MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0