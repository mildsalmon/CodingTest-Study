from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)

    weak_long = weak + [weak[i] + n for i in range(len(weak))]

    dist_permu = list(permutations(dist))

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])