"""
Date    : 2021.12.14
Update  : 2021.12.14
Source  : 등수 매기기.py
Purpose : 계수정렬과 그리디를 이용하여 해결하였다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def rank(counting_sort):
    """
    인덱스 에러
    :param counting_sort:
    :return:
    """
    real_rank = []
    predict_rank = []
    answer = 0
    count = 0

    for i in range(1, len(counting_sort)):
        if counting_sort[i] != 1:
            if counting_sort[i] >= 2:
                predict_rank.extend([i] * (counting_sort[i] - 1))
            elif counting_sort[i] == 0:
                real_rank.append(i)
                count += 1

    for i in range(count):
        temp = predict_rank[i] - real_rank[i]
        answer += abs(temp)

    return answer

if __name__ == "__main__":
    n = int(input())
    counting_sort = [0] * (n+1)

    for _ in range(n):
        temp = int(input())
        counting_sort[temp] += 1

    print(rank(counting_sort))