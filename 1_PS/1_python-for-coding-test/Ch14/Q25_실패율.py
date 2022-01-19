def solution(N, stages):
    # fail_per = [0] * (N + 1)
    no_clear = [0] * (N + 1)
    player_count = [0] * (N + 1)
    answer = []

    for stage in stages:
        no_clear[stage - 1] += 1

        for i in range(stage):
            player_count[i] += 1

    fail_per = [0] * (N + 1)

    for i in range(N + 1):
        if no_clear[i] == 0 or player_count[i] == 0:
            fail_per[i] = [i, 0]
        else:
            fail_per[i] = [i, (no_clear[i] / player_count[i])]

    fail_per = fail_per[:N]
    fail_per.sort(reverse=True, key=lambda x: [x[1], -x[0]])

    for i in fail_per:
        answer.append(i[0] + 1)

    return answer

# 16분
solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3])