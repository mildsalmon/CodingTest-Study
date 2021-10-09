def solution(lottos, win_nums):
    count = 0
    zero_count = 0
    answer = []

    for i in range(6):
        if lottos[i] in win_nums:
            count += 1
        if lottos[i] == 0:
            zero_count += 1

    max_rank = count + zero_count
    min_rank = count

    for i in [max_rank, min_rank]:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        elif i <= 1:
            answer.append(6)

    return answer