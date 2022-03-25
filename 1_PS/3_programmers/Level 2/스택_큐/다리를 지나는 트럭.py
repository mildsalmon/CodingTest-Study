"""
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 다리를 지나는 트럭.py
Purpose : queue / stack
url     : https://programmers.co.kr/learn/courses/30/lessons/42583
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    now_weight = 0

    while bridge:
        now_weight -= bridge.pop(0)

        if truck_weights:
            if now_weight + truck_weights[0] <= weight:
                temp = truck_weights.pop(0)
                now_weight += temp
                bridge.append(temp)
            else:
                bridge.append(0)

        answer += 1

    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])

# 정확성  테스트
# 테스트 1 〉	통과 (0.64ms, 10.3MB)
# 테스트 2 〉	통과 (49.64ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (8.90ms, 10.3MB)
# 테스트 5 〉	통과 (295.82ms, 10.3MB)
# 테스트 6 〉	통과 (39.07ms, 10.3MB)
# 테스트 7 〉	통과 (0.44ms, 10.4MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (2.10ms, 10.4MB)
# 테스트 10 〉	통과 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.17ms, 10.2MB)
# 테스트 13 〉	통과 (0.60ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
#
# 채점 결과
# 정확성: 92.9
# 합계: 92.9 / 100.0