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
    인덱스 에러 해결
    :param counting_sort:
    :return:
    """
    global n

    real_rank = []
    predict_rank = []
    answer = 0

    for i in range(1, len(counting_sort)):
        # if counting_sort[i] != 1:
        if counting_sort[i] >= 1 and i > n:
            predict_rank.extend([i] * counting_sort[i])
        elif counting_sort[i] >= 2:
            predict_rank.extend([i] * (counting_sort[i] - 1))
        elif counting_sort[i] == 0:
            real_rank.append(i)

    for i in range(len(predict_rank)):
        temp = predict_rank[i] - real_rank[i]
        answer += abs(temp)

    return answer

if __name__ == "__main__":
    n = int(input())
    counting_sort = [-1] * (500001)

    array = []

    for i in range(1, n+1):
        temp = int(input())
        array.append(temp)
        counting_sort[temp] = 0
        counting_sort[i] = 0

    for a in array:
        counting_sort[a] += 1

    print(rank(counting_sort))