"""
Date    : 2022.03.25
Update  : 2022.03.27
Source  : 다리를 지나는 트럭.py
Purpose : queue / stack
url     : https://programmers.co.kr/learn/courses/30/lessons/42583
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridges = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    last_weight = 0
    time = 0

    while bridges:
        truck = bridges.popleft()
        last_weight -= truck
        time += 1

        if truck_weights:
            if last_weight + truck_weights[0] > weight:
                bridges.append(0)
                continue

            truck = truck_weights.popleft()
            bridges.append(truck)
            last_weight += truck

    return time

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])

# 정확성  테스트
# 테스트 1 〉	통과 (0.42ms, 10.4MB)
# 테스트 2 〉	통과 (6.68ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (5.38ms, 10.4MB)
# 테스트 5 〉	통과 (49.69ms, 10.3MB)
# 테스트 6 〉	통과 (22.20ms, 10.3MB)
# 테스트 7 〉	통과 (0.63ms, 10.2MB)
# 테스트 8 〉	통과 (0.13ms, 10.2MB)
# 테스트 9 〉	통과 (1.93ms, 10.2MB)
# 테스트 10 〉	통과 (0.15ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.4MB)
# 테스트 12 〉	통과 (0.25ms, 10.2MB)
# 테스트 13 〉	통과 (0.51ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
#
# 채점 결과
# 정확성: 92.9
# 합계: 92.9 / 100.0