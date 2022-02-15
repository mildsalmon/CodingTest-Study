"""
Date    : 2022.02.15
Update  : 2022.02.15
Source  : 주차 요금 계산.py
Purpose : 수학 / dict / map / lambda
url     : https://programmers.co.kr/learn/courses/30/lessons/92341
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import defaultdict


def search_parking_time(records: list) -> dict:
    cars = defaultdict(list)

    for record in records:
        time, number, action = record.split()
        hh, mm = list(map(int, time.split(':')))
        convert_time = (hh * 60) + mm
        cars[number].append([convert_time, action])

    return cars


def calculation_pay(cars: dict, fees: list) -> dict:
    pays = dict()

    for car, values in cars.items():
        if len(values) % 2 != 0:
            max_time = (23 * 60) + 59
            values.append([max_time, 'OUT'])
            # values.append(max_time)
        IN_total = 0
        OUT_total = 0
        for value in values:
            time, action = value

            if action == 'IN':
                IN_total += time
            elif action == 'OUT':
                OUT_total += time

        parking_time = OUT_total - IN_total

        if parking_time <= fees[0]:
            pays[car] = fees[1]
        elif parking_time > fees[0]:
            excess_time = (parking_time - fees[0])

            if excess_time % fees[2]:
                excess_time = (excess_time // fees[2]) + 1
            else:
                excess_time = excess_time // fees[2]

            pays[car] = fees[1] + (excess_time * fees[3])

    return pays


def solution(fees, records):
    cars = search_parking_time(records)
    pays = calculation_pay(cars, fees)

    answer = sorted(pays.items(), key=lambda x: x[0])

    return list(map(lambda x: x[1], answer))

# 채점을 시작합니다.
#
# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.5MB)
# 테스트 4 〉	통과 (0.09ms, 10.4MB)
# 테스트 5 〉	통과 (0.33ms, 10.4MB)
# 테스트 6 〉	통과 (0.21ms, 10.3MB)
# 테스트 7 〉	통과 (1.81ms, 10.4MB)
# 테스트 8 〉	통과 (1.11ms, 10.4MB)
# 테스트 9 〉	통과 (0.36ms, 10.4MB)
# 테스트 10 〉	통과 (1.62ms, 10.5MB)
# 테스트 11 〉	통과 (2.15ms, 10.8MB)
# 테스트 12 〉	통과 (2.20ms, 10.8MB)
# 테스트 13 〉	통과 (0.05ms, 10.5MB)
# 테스트 14 〉	통과 (0.04ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.4MB)
#
# 채점 결과
#
# 정확성: 100.0
#
# 합계: 100.0 / 100.0