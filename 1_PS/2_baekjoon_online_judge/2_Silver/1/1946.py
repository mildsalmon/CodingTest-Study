"""
Date    : 2021.11.28
Update  : 2021.11.28
Source  : 1946.py
Purpose : 1차 성적 또는 2차 성적이 다른 사람보다 높은 신입사원만 채용하는 코드를 작성하라.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

# 1차 성적으로 정렬하고, 1차 성적 1등의 2차 성적을 저장한다.
# 1차 성적 2등부터 꼴등까지 개인별 2차 성적과 2차 성적 최솟값을 비교한다.
# 만약, 2차 성적 최솟값보다 크다면, 탈락
# 2차 성적 최솟값보다 작다면, 합격

for tc in range(int(input())):
    n = int(input())
    array = []
    # 2차 성적 최솟값 저장
    second_test_min = 0
    # 1차 성적 1등은 어떤 경우에도 합격이기 때문에, 초기값을 1로 초기화함.
    max_count = 1

    for i in range(n):
        array.append(list(map(int, input().split())))

    # 1차 성적으로 오름차순 정렬한다.
    array.sort(key=lambda x:x[0])
    # 1차 성적 1등의 2차 성적을 저장한다.
    # 추후 이 값과 비교하여 합격 여부를 판단한다.
    second_test_min = array[0][1]

    # 1차 성적 1등을 제외한 나머지 지원자들을 비교
    for i in range(1, n):
        # 2차 성적 최소값보다 작다면, 합격 그리고 2차 성적 갱신
        if array[i][1] < second_test_min:
            max_count += 1
            second_test_min = array[i][1]

    print(max_count)
