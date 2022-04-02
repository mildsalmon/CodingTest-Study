"""
Date    : 2022.03.28
Update  : 2022.03.28
Source  : 소수 찾기.py
Purpose : dfs / 완전 탐색 / 재귀 / 소수
url     : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def per_num(depth, numbers, visited, number):
    global n, answer

    if depth == n:
        print(number)
        if number:
            if int(number) in answer:
                return
            if is_prime(int(number)):
                answer.add(int(number))
        return

    for i, value in enumerate(numbers):
        if visited[i]:
            per_num(depth + 1, numbers, visited, number)
            continue
        visited[i] = True
        per_num(depth + 1, numbers, visited, number + value)
        visited[i] = False


def solution(numbers):
    global n, answer

    answer = set()
    n = len(numbers)
    visited = [False for _ in range(len(numbers))]

    per_num(0, numbers, visited, '')
    return len(answer)

solution('17')

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (2.60ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (1.17ms, 10.6MB)
# 테스트 5 〉	통과 (5.76ms, 11.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.4MB)
# 테스트 8 〉	통과 (5.29ms, 11.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (5.48ms, 10.4MB)
# 테스트 11 〉	통과 (0.57ms, 10.3MB)
# 테스트 12 〉	통과 (0.21ms, 10.1MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0