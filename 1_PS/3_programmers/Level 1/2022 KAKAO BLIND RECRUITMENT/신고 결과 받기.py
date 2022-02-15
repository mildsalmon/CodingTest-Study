"""
Date    : 2022.02.14
Update  : 2022.02.14
Source  : 신고 결과 받기.py
Purpose : dict / 해시
url     : https://programmers.co.kr/learn/courses/30/lessons/92334
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(id_list, report, k):
    report = set(report)

    report_dict = {key: 0 for key in id_list}
    id_dict = dict.fromkeys(id_list, 0)

    for value in report:
        user_id, report_id = value.split()

        report_dict[report_id] += 1

    for value in report:
        user_id, report_id = value.split()

        if report_dict[report_id] >= k:
            id_dict[user_id] += 1

    return list(id_dict.values())

# 채점을 시작합니다.
#
# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (147.61ms, 39.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.91ms, 10.3MB)
# 테스트 7 〉	통과 (1.55ms, 10.7MB)
# 테스트 8 〉	통과 (1.95ms, 10.9MB)
# 테스트 9 〉	통과 (63.95ms, 23.8MB)
# 테스트 10 〉	통과 (55.59ms, 23.6MB)
# 테스트 11 〉	통과 (137.13ms, 39.3MB)
# 테스트 12 〉	통과 (0.21ms, 10.3MB)
# 테스트 13 〉	통과 (0.19ms, 10.3MB)
# 테스트 14 〉	통과 (48.11ms, 19.8MB)
# 테스트 15 〉	통과 (69.18ms, 31.3MB)
# 테스트 16 〉	통과 (0.14ms, 10.2MB)
# 테스트 17 〉	통과 (0.19ms, 10.3MB)
# 테스트 18 〉	통과 (0.52ms, 10.1MB)
# 테스트 19 〉	통과 (0.61ms, 10.3MB)
# 테스트 20 〉	통과 (53.51ms, 20.1MB)
# 테스트 21 〉	통과 (78.39ms, 31.3MB)
# 테스트 22 〉	통과 (0.01ms, 10.1MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
#
# 채점 결과
#
# 정확성: 100.0
#
# 합계: 100.0 / 100.0