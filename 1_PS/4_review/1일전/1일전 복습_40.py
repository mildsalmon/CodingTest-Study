# 가사 검색

from bisect import bisect_left, bisect_right


def count_range(array, left, right):
    l = bisect_left(array, left)
    r = bisect_right(array, right)

    return r - l


def solution(words, queries):
    array_words = [[] for i in range(10001)]
    reverse_array_words = [[] for i in range(10001)]

    for word in words:
        array_words[len(word)].append(word)
        reverse_array_words[len(word)].append(word[::-1])

    for i in range(len(array_words)):
        if len(array_words) != 0:
            array_words[i].sort()
            reverse_array_words[i].sort()

    count_answer = [0] * (len(queries))

    for i, query in enumerate(queries):
        temp = 0
        if len(array_words[len(query)]) != 0:
            if query[0] == '?':
                temp = count_range(reverse_array_words[len(query)], query[::-1].replace('?', 'a'),
                                   query[::-1].replace('?', 'z'))
            elif query[-1] == '?':
                temp = count_range(array_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        count_answer[i] = temp

    #     for i, query in enumerate(queries):
    #         if len(array_words[len(query)]) != 0:
    #             if query[0] == '?':
    #                 # end_pos = len(query) - query[::-1].index('?')
    #                 end_pos = bisect_right(query, 'A')
    #                 for array_word in array_words[len(query)]:
    #                     if array_word[end_pos:] == query[end_pos:]:
    #                         count_answer[i] += 1

    #             elif query[-1] == '?':
    #                 # start_pos = query.index('?')
    #                 start_pos = len(query) - bisect_right(query[::-1], 'A')

    #                 for array_word in array_words[len(query)]:
    #                     if array_word[:start_pos] == query[:start_pos]:
    #                         count_answer[i] += 1
    #         else:
    #             count_answer[i] = 0

    return count_answer