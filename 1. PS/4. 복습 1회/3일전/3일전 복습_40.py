# 가사 검색

from bisect import bisect_right, bisect_left


def counting_range(array, left, right):
    l = bisect_left(array, left)
    r = bisect_right(array, right)
    # print(array)
    # print(left)
    # print(right)
    # print(l, r)
    # print()
    return r - l


def solution(words, queries):
    word_reverse = [[] for i in range(10001)]
    word_list = [[] for i in range(10001)]
    answer = []

    for word in words:
        word_list[len(word)].append(word)
        word_reverse[len(word)].append(word[::-1])

    for i in range(10001):
        if len(word_list) != 0:
            word_list[i].sort()
            word_reverse[i].sort()

    for query in queries:
        if query[0] == '?':
            # ? 시작
            temp = counting_range(word_reverse[len(query)], query[::-1].replace('?', 'a'),
                                  query[::-1].replace('?', 'z'))

        elif query[-1] == '?':
            # ? 끝
            temp = counting_range(word_list[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(temp)
    return answer