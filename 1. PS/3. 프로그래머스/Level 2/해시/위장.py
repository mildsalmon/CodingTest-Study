"""
Date    : 2021.12.17
Update  : 2021.12.17
Source  : 위장.py
Purpose : 딕셔너리 values의 길이를 조합에 넣고 계산. (시간초과)
url     : https://programmers.co.kr/learn/courses/30/lessons/42578
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import combinations

def solution(clothes):
    clothes_dict = {}
    answer = 0
    kind_len = 0

    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
        kind_len += 1

    clothes_len_list = list(clothes_dict.values())

    for i in range(1, kind_len + 1):
        # 조합에서 시간초과가 발생했을 것이다.
        # 만약, 옷의 종류가 30가지라면 $_{30}C_{15}$ (n=30, r=15인 조합)의 경우 155,117,520개가 발생하므로 시간초과가 당연하다.
        for combi in list(combinations(clothes_len_list, i)):
            temp = combi[0]
            for j in range(1, i):
                temp *= combi[j]
            answer += temp

    return answer

# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.12ms, 10.2MB)
# 테스트 4 〉	통과 (171.36ms, 16.5MB)
# 테스트 5 〉	통과 (0.07ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (196.57ms, 16.4MB)
# 테스트 8 〉	통과 (1.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (5.09ms, 10.5MB)
# 테스트 13 〉	통과 (19.09ms, 11.7MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.02ms, 10.2MB)
# 테스트 18 〉	통과 (0.12ms, 10.2MB)
# 테스트 19 〉	통과 (1.07ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.02ms, 10.3MB)
# 테스트 24 〉	통과 (0.02ms, 10.3MB)
# 테스트 25 〉	통과 (0.52ms, 10.3MB)
# 테스트 26 〉	통과 (386.86ms, 22.9MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.49ms, 10.2MB)
#
# 채점 결과
# 정확성: 96.4
# 합계: 96.4 / 100.0