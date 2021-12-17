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
    answer = 1

    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    """
    [[얼굴A],
     [얼굴B],
     [하의A],
     [얼굴A, 하의A],
     [얼굴B, 하의A]]
    
    위 경우는 아래처럼 생각할 수 있다.
    
    [[얼굴A, 하의x],
     [얼굴B, 하의x],
     [얼굴x, 하의A],
     [얼굴A, 하의A],
     [얼굴B, 하의A],
     [얼굴x, 하의x]]
    여기서 하루에 최소 한 개의 의상은 입는다고 했으므로 [얼굴x, 하의x]를 제외해준다.
    """
    for _, value in clothes_dict.items():
        answer *= (value + 1)
    answer -= 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.1MB)
# 테스트 10 〉	통과 (0.00ms, 10MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.00ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.00ms, 10.2MB)
# 테스트 22 〉	통과 (0.00ms, 10.1MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.1MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.00ms, 10.3MB)
# 테스트 28 〉	통과 (0.01ms, 10.3MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0