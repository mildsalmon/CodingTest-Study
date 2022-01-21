import heapq


def solution(jobs):
    jobs.sort(key=lambda x: [-x[0], -x[1]])

    wait_queue = [jobs.pop()[::-1]]
    acc = 0
    work_count = 0
    answer = 0

    while wait_queue:
        time = heapq.heappop(wait_queue)
        acc += time[0]
        work_count += 1
        answer += (acc - time[1])

        while jobs:
            if jobs[-1][0] <= acc:
                heapq.heappush(wait_queue, jobs.pop()[::-1])
            else:
                if len(wait_queue) == 0:
                    temp = jobs.pop(0)[::-1]
                    heapq.heappush(wait_queue, jobs.pop()[::-1])
                    acc = temp[1]
                break

    return answer // work_count




