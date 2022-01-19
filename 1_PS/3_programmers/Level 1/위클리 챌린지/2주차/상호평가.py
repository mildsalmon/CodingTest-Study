def solution(scores):
    arrays = []

    for i in zip(*scores):
        arrays.append(i)

    # print(array)
    answers = []

    for i in range(len(arrays)):
        me = arrays[i][i]
        max_array = max(arrays[i])
        min_array = min(arrays[i])

        temp = sum(arrays[i])
        temp_len = len(arrays[i])

        if (me == max_array and arrays[i].count(me) == 1) or (me == min_array and arrays[i].count(me) == 1):
            temp -= me
            temp_len -= 1

        answers.append(temp / temp_len)
    # print(answers)
    grade = ''

    for answer in answers:
        if 90 <= answer:
            grade += 'A'
        elif 80 <= answer < 90:
            grade += 'B'
        elif 70 <= answer < 80:
            grade += 'C'
        elif 50 <= answer < 70:
            grade += 'D'
        elif answer < 50:
            grade += 'F'

    return grade