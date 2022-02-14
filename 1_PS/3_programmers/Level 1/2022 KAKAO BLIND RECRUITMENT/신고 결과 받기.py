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

    report_dict = dict()
    id_dict = dict.fromkeys(id_list, 0)

    for value in report:
        user_id, report_id = value.split()

        if report_id in report_dict:
            report_dict[report_id].append(user_id)
        else:
            report_dict[report_id] = [user_id]

    for key, value in report_dict.items():
        if len(value) >= k:
            for id in value:
                id_dict[id] += 1

    return list(id_dict.values())

# 채점을 시작합니다.
#
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (141.33ms, 46.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.72ms, 10.6MB)
# 테스트 7 〉	통과 (1.16ms, 10.7MB)
# 테스트 8 〉	통과 (1.59ms, 10.9MB)
# 테스트 9 〉	통과 (57.57ms, 27.2MB)
# 테스트 10 〉	통과 (55.30ms, 26.8MB)
# 테스트 11 〉	통과 (137.73ms, 46.3MB)
# 테스트 12 〉	통과 (0.19ms, 9.96MB)
# 테스트 13 〉	통과 (0.25ms, 10.2MB)
# 테스트 14 〉	통과 (47.26ms, 24.4MB)
# 테스트 15 〉	통과 (60.41ms, 36.4MB)
# 테스트 16 〉	통과 (0.12ms, 10.2MB)
# 테스트 17 〉	통과 (0.16ms, 10.2MB)
# 테스트 18 〉	통과 (0.32ms, 10.3MB)
# 테스트 19 〉	통과 (0.50ms, 10.3MB)
# 테스트 20 〉	통과 (41.70ms, 24MB)
# 테스트 21 〉	통과 (81.22ms, 36.6MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.3MB)
#
# 채점 결과
#
# 정확성: 100.0
#
# 합계: 100.0 / 100.0