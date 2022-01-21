import heapq

def solution(jobs):
    jobs.sort(key=lambda x:[-x[0], -x[1]])

    work_count = len(jobs)
    temp = jobs.pop()[::-1]
    wait_queue = [temp]
    acc = temp[1]
    answer = 0

    while wait_queue:
        time = heapq.heappop(wait_queue)
        acc += time[0]
        answer += (acc - time[1])

        while jobs:
            if jobs[-1][0] <= acc:
                heapq.heappush(wait_queue, jobs.pop()[::-1])
            else:
                if len(wait_queue) == 0:
                    temp = jobs.pop()[::-1]
                    heapq.heappush(wait_queue, temp)
                    acc = temp[1]
                break

    return answer // work_count



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
# 테스트 1 〉	통과 (0.64ms, 10.3MB)
# 테스트 2 〉	통과 (1.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.55ms, 10.3MB)
# 테스트 4 〉	통과 (0.48ms, 10.3MB)
# 테스트 5 〉	통과 (0.72ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.43ms, 10.2MB)
# 테스트 8 〉	통과 (0.31ms, 10.3MB)
# 테스트 9 〉	통과 (0.12ms, 10.3MB)
# 테스트 10 〉	통과 (0.74ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0