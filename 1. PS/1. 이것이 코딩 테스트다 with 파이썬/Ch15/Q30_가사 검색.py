def solution(words, queries):
    answer_count = [0] * len(queries)

    for i, query in enumerate(queries):
        query_len = len(query)

        question_first = query.find('?')
        question_count = query.count('?')
        question_last = question_first + question_count

        # ?가 앞에 있음
        if question_first == 0:
            for word in words:
                if len(word) == len(query):
                    if word[question_last:query_len] == query[question_last:query_len]:
                        answer_count[i] += 1
        # ?가 뒤에 있음
        elif question_last == query_len:
            for word in words:
                if len(word) == len(query):
                    if word[0:question_first] == query[0:question_first]:
                        answer_count[i] += 1
                        # print(word, "|", query)
        # print()
    # print(answer_count)
    return answer_count

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])