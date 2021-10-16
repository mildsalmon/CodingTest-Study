from collections import deque
import math


def solution(progresses, speeds):
    q = deque()

    for i, progress in enumerate(progresses):
        temp = 100 - progress
        temp = math.ceil(temp / speeds[i])
        q.append((progress, temp))

    answer = [1]
    p, time = q.popleft()

    while q:
        x_p, x_time = q.popleft()

        if x_time <= time:
            answer[-1] += 1
        elif x_time > time:
            answer.append(1)
            time = x_time

    return answer
