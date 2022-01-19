# 상호평가

def solution(scores):
    transpose_scores = []
    answer = []
    rank = ['A', 'B', 'C', 'D', 'F']

    for i in zip(*scores):
        transpose_scores.append(i)
        answer.append([len(transpose_scores[-1]), sum(transpose_scores[-1])])

    for i in range(len(transpose_scores)):
        min_value = min(transpose_scores[i])
        max_value = max(transpose_scores[i])
        if transpose_scores[i][i] == min_value and transpose_scores[i].count(min_value) == 1:
            answer[i][0] -= 1
            answer[i][1] -= min_value
        elif transpose_scores[i][i] == max_value and transpose_scores[i].count(max_value) == 1:
            answer[i][0] -= 1
            answer[i][1] -= max_value

    result = [i[1] / i[0] for i in answer]

    answer_label = ''

    for r in result:
        if 90 <= r:
            answer_label += rank[0]
        elif 80 <= r < 90:
            answer_label += rank[1]
        elif 70 <= r < 80:
            answer_label += rank[2]
        elif 50 <= r < 70:
            answer_label += rank[3]
        elif r < 50:
            answer_label += rank[4]

    return answer_label

# 멀쩡한 사각형

import math


def solution(w, h):
    g = math.gcd(w, h)

    if g == 1:
        fill_count = w + h - 1
    elif g > 1:
        fill_count = g * ((w // g) + (h // g) - 1)

    return w * h - fill_count

# 124 나라의 숫자

def solution(n):
    rule = ['1', '2', '4']
    answer = ''

    while n > 0:
        n -= 1
        answer = rule[n % 3] + answer

        n //= 3

    return answer