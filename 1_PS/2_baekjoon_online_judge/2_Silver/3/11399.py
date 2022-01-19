"""
Date    : 2021.11.28
Update  : 2021.11.28
Source  : 11399.py
Purpose : CPU Scheduling 중 SJF가 떠올랐다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

# 운영체제 과목 - CPU Scheduling
# 문제를 읽어보고 `비선점 최소작업 우선 스케줄링 (SJF)`가 떠올랐다.
# 단, 새로운 프로세스가 특정 시간에 프로세스가 들어오는 것이 아닌,
# 0초(초기)에 프로세스가 전부 들어오고 cpu burst time을 확인하고, 짧은 작업부터 시작한다.

n = int(input())

array = list(map(int, input().split()))

# 최소작업부터 시작해야하므로, 오름차순으로 정렬한다.
array.sort()

# wait time을 따로 저장하고 누적합을 진행한다.
wait_time = 0
answer = 0

for p in array:
    wait_time += p
    answer += wait_time

print(answer)