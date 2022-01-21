import heapq


def solution(jobs):
    jobs.sort(key=lambda x: [x[0]])

    work_count = len(jobs)
    temp = jobs.pop(0)[::-1]
    wait_queue = [temp]
    acc = temp[1]
    answer = 0

    while wait_queue:
        time = heapq.heappop(wait_queue)
        acc += time[0]
        answer += (acc - time[1])

        while jobs:
            if jobs[0][0] <= acc:
                heapq.heappush(wait_queue, jobs.pop(0)[::-1])
            else:
                if len(wait_queue) == 0:
                    temp = jobs.pop(0)[::-1]
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

#### 아래 테케 틀림
print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74
###

# 테케 출처
# https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html