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
    current_weight = [truck_weights.pop(0)]
    flag = True

    while True:
        while sum(current_weight) + sum(truck_weights[:1]) <= weight:
            if truck_weights:
                current_weight.append(truck_weights.pop(0))
                answer += 1
            else:
                # current_weight
                break
        answer += bridge_length
        current_weight = [current_weight[-1]]

        if len(current_weight) == 0 and len(truck_weights) == 0:
            break

    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])