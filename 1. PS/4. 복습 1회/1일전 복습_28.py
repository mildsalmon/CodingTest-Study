from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    answer = len(dist) + 1
    weak_copy = weak[:] + [weak[i] + n for i in range(weak_len)]

    for w_l in range(weak_len):
        for p in list(permutations(dist, len(dist))):
            count = 1
            temp = weak_copy[w_l] + p[0]
            for i in range(w_l, w_l + weak_len):
                if temp < weak[i]:
                    temp = weak_copy[i] + p[count]
                    count += 1
                if count > len(dist):
                    return -1
            answer = min(answer, count)

    return answer



solution(12, [1, 5, 6, 10], [1, 2, 3, 4])